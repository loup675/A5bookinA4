# A5bookinA4
Prepare your A5 books to print in A4 pages.

# Dependencies: 

pypdf, pymupdf and **numpy** ~~which i forgor to add in the notebook description~~ (just for some sorting, if you know something else you can use it). os and re (for renaming bookbinder app output) should come preinstalled.

You can install these using pip:

```
pip install pypdf pymupdf numpy
```

Also rember to [make a virtual environment for this!](https://www.youtube.com/watch?v=Y21OR1OPC9A)

# How to use

Make your A5 book in [bookbinder app](https://bookbinder.app/), 2 pages per side and scaled pages. Sheets per signature can technically be how many as you want, but I personally usually use 5.

# References

[fetch all pdf files function from this notebook from a github page, which is from a youtube tutoyial](https://github.com/Jcharis/DataScienceTools/blob/master/PyPDF_CrashCourse/PyPDF2%20Crash%20Course.ipynb)

[pypdf merging pdfs](https://pypdf.readthedocs.io/en/stable/user/merging-pdfs.html)

[pypdf's guide to transforming several of copies of the same page](https://pypdf.readthedocs.io/en/stable/user/cropping-and-transforming.html#transforming-several-copies-of-the-same-page) (ended up not using it, since i moved onto pymupdf, but good to take note of this!!)

[pymupdf's guide to combining single pages](https://pymupdf.readthedocs.io/en/latest/the-basics.html#combining-single-pages)

[pymupdf's rect documentation](https://pymupdf.readthedocs.io/en/latest/rect.html) (had to understand this since I wanted to make a 2up instead of 4up as in the example above!)

Unfortunately, the functions for renaming the outputs from [bookbinder app](https://bookbinder.app/) is AI-sloppa (deep-seek). As stated in the cell that contains it, I was too tired to figure it out and none of the intricate requirements I needed were in any tutorial help I found on google/stackexchange, so I gave it a shot and it fortunately didn't have much problem figuring it out.
