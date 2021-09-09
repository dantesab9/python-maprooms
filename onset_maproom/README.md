# Onset Maproom

This directory contains a Dash recreation of the
[Ethiopia NMA "Onset" Maproom](http://213.55.84.78:8082/maproom/Agriculture/Historical/Onset.html).
This maproom is a testbed for future Dash-based maprooms and will be
generalized further in the future.


# Installation and Run Instructions

* Install Miniconda: https://docs.conda.io/en/latest/miniconda.html

* Create conda environment `enactsmaproom` as follows:

    `conda env create -f environment.yml -n enactsmaproom`

* Activate conda environment `enactsmaproom` as follows:

    `conda activate enactsmaproom`

* Run application as follows:

    `CONFIG=config-sample.yaml python maproom.py`

* Navigate your browser to `http://127.0.0.1:8050/onset-maproom/`

* When done using the maproom stop Dash with CTRL-C and deactivate the `enactsmaproom` environment with:

    `conda deactivate`

# Development Instructions

This maproom is structured around four different files:

* `layout.py`: functions which generate the general layout of the maproom

* `maproom.py`: callbacks for user interaction

* `charts.py`: code for generating URLs for dlcharts/dlsnippets/ingrid charts and/or fetching table data

* `widgets.py`: routines for common maproom components.

The widgets module contains a few functions of note:

* `Body()`: The first parameter is a string which is the title of the layout block.
   After the first, this function allows for a variable number of Dash components.

* `Sentence()`: Many maprooms have forms in a "sentence" structure where input fields are interspersed
  within a natural language sentence. This function abstracts this functionality. It requires that
  the variable number of arguments alternate between a string and a dash component.

* `Date()`: This is a component for a date selector. The first argument is the HTML id,
  the second is the default day of month, and the third is the default month (in three-letter abbreviated form)

* `Number()`: This is a component for a number selector. The first argument is the HTML id,
   the second and third are the lower and upper bound respectively.


# Support

* `kgraaf@iri.columbia.edu`