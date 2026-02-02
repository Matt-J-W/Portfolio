library(reticulate)

# Tell reticulate to use the r-reticulate environment
use_condaenv("r-reticulate", required = TRUE)

# Install your Python packages into that environment
py_install(c("pandas", "openpyxl", "seaborn", "matplotlib", "scikit-learn", "jinja2", "ipython", "tabulate"), pip = TRUE)

  # rmarkdown::render_site()