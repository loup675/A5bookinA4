import os
def fetch_all_pdf_files(parent_folder: str):
    target_files = []
    for path, subdirs, files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path, name))
    return target_files 

def imposition(n: int, pages_per_signature: int = 20):
    """
    Return (fronts, backs) for printing a book of n pages.
    pages_per_signature should be a multiple of 4 (default 20 = 5 sheets).
    The last signature is padded with None to a multiple of 4.
    """
    fronts = []
    backs = []
    start = 1

    while start <= n:
        remaining = n - start + 1
        size = min(pages_per_signature, remaining)
        # Pad to next multiple of 4
        padded_size = ((size + 3) // 4) * 4
        pages = list(range(start, start + size)) + [None] * (padded_size - size)

        # Build sheets for this signature
        for i in range(padded_size // 4):
            # local 1-based indices mapped to 0-based list
            fl = pages[padded_size - 2*i - 1]   # front left
            fr = pages[1 + 2*i - 1]             # front right
            bl = pages[2 + 2*i - 1]             # back left
            br = pages[padded_size - 1 - 2*i - 1]  # back right

            fronts.extend([fl, fr])
            backs.extend([bl, br])

        start += size

    return fronts, backs

def impose(book_name):
    import pymupdf
    src = pymupdf.open(f"{book_name}.pdf")
    n = len(src)

    combined_doc = pymupdf.open()

    # --- same rectangle setup as your code --- # -> pymupdf 4-up rect setup
    width, height = pymupdf.paper_size("a4")
    r = pymupdf.Rect(0, 0, width, height)
    r1 = r / 2
    r2 = r1 + (r1.width, 0, r1.width, 0)
    r3 = r1 + (0, r1.height, 0, r1.height)
    r4 = pymupdf.Rect(r1.br, r.br)
    r_tab = [r1, r2, r3, r4]        # TL, TR, BL, BR

    front, back = imposition(n)

    def place_quad(doc, quad):
        page = doc.new_page(-1, width=width, height=height)
        for rect, pno in zip(r_tab, quad):
            if pno is None:
                continue
            page.show_pdf_page(rect, src, pno - 1)

    # --- one pass, interleaved: F0, B0, F1, B1, ... ---
    combined = pymupdf.open()
    for i in range(0, len(front), 4):
        fq = front[i:i+4]
        bq = back [i:i+4]
        place_quad(combined, fq)    # front of sheet i/4
        place_quad(combined, bq)    # back  of sheet i/4

    combined.save(f"[final] {book_name}.pdf", garbage=3, deflate=True)

if __name__ == "__main__":
    pdf_list = fetch_all_pdf_files("./")
    print(pdf_list)
    book_name = input("Please enter a valid pdf name: ")
    if book_name not in pdf_list:
        print("Please rerun the script and input a valid pdf name!")
    else:
        impose(book_name)