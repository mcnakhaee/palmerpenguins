import pandas as pd
import pkg_resources
import numpy as np
import os
from os.path import dirname, exists, expanduser, isdir, join, splitext


def load_penguins(return_X_y=False,drop_na = False):
    """Load and return the penguins dataset (classification).

      The Palmer penguins dataset is a dataset for data exploration & visualization, and can be used as an
      alternative to the Iris dataset.
      =================   ==============
      Classes                          3
      Samples per class        [152,168,124]
      Samples total                  344
      Dimensionality                  8
      Features            real, integer, string, positive
      =================   ==============
      Read more in the :ref:`https://github.com/allisonhorst/palmerpenguins>`.
      Parameters
      ----------
      return_X_y : bool, default=False
          If True, returns a ``(data, target)`` tuple instead of a dataframe object.
          See below for more information about the `data` and `target` object.
      drop_na: bool, default=False
      If True drop rows from dataset that contain missing values. Only available when `return_X_y = True`

      Returns
      -------
      data : :class:`pandas.core.frame.DataFrame`
          data is a dataframe of shape (344  , 8) and has the following columns:
      =================   ==============
      species              a string denoting penguin species (Adélie, Chinstrap and Gentoo)
      island               a string denoting island in Palmer Archipelago, Antarctica (Biscoe, Dream or Torgersen)
      bill_length_mm       a number denoting bill length (millimeters)
      bill_depth_mm        a number denoting bill depth (millimeters)
      flipper_length_mm    an integer denoting flipper length (millimeters)
      body_mass_g          an integer denoting body mass (grams)
      sex                  a string denoting penguin sex (female, male)
      year                 an integer denoting the study year (2007, 2008, or 2009)
      =================   ==============

      (data, target) : tuple if ``return_X_y`` is True
          data : a dataframe of shape (344  , 4)  where each column corresponds to one of the four size measurements of penguins including bill_length_mm, bill_depth_mm, flipper_length_mm and body_mass_g.
          target: {ndarray, Series} of shape (344,)
              The classification target (i.e. penguin species).
      --------
      Let's say you are interested in the samples 10, 80, and 140, and want to
      know their class name.
      >>> from palmerpenguins.penguins import load_penguins
      >>> penguins = load_penguins()
      >>> list(penguins.iloc[[1, 160, 300],0])
      ['Adelie', 'Gentoo', 'Chinstrap']
      >>> dict(pd.value_counts(penguins.species))
      {'Adelie': 152, 'Gentoo': 124, 'Chinstrap': 68}
      """

    stream = pkg_resources.resource_stream(__name__, 'data/penguins.csv')
    penguins = pd.read_csv(stream)
    if return_X_y:
        if drop_na:
            penguins.dropna(inplace = True)
        data = penguins[['bill_length_mm', 'bill_depth_mm',
                         'flipper_length_mm', 'body_mass_g']]
        target = penguins['species']


        return data, target

    return penguins


def load_penguins_raw():
    """Load and return the raw penguins dataset (classification).
      Data were collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.
      It Includes all the variables and original names, nesting observations, penguin size data, and isotope measurements from blood samples for adult Adélie, Chinstrap, and Gentoo penguins.
      =================   ==============
      Classes                          3
      Samples per class        [152,168,124]
      Samples total                  344
      Dimensionality                  17
      Features            real, integer, string, positive
      =================   ==============




      Read more in the :ref:`https://github.com/allisonhorst/palmerpenguins`.

      Returns
      -------
      data : :class:`pandas.core.frame.DataFrame`
          data : a dataframe of shape (344  , 17) and has the following columns:

          Columns
      =================   ==============
      studyName            Sampling expedition from which data were collected, generated, etc.
      Sample Number        an integer denoting the continuous numbering sequence for each sample
      Species              a string denoting the penguin species
      Region               a string denoting the region of Palmer LTER sampling grid
      Island               a string denoting the island near Palmer Station where samples were collected
      Stage                a character string denoting reproductive stage at sampling
      Individual ID        a string denoting the unique ID for each individual in dataset
      Clutch Completion    a string denoting if the study nest observed with a full clutch, i.e., 2 eggs
      Date Egg             a date denoting the date study nest observed with 1 egg (sampled)
      Culmen Length        a number denoting the length of the dorsal ridge of a bird's bill (millimeters)
      Culmen Depth         a number denoting the depth of the dorsal ridge of a bird's bill (millimeters)
      Flipper Length       an integer denoting the length penguin flipper (millimeters)
      Body Mass            an integer denoting the penguin body mass (grams)
      Sex                  a character string denoting the sex of an animal
      Delta 15 N           a number denoting the measure of the ratio of stable isotopes 15N:14N
      Delta 13 C           a number denoting the measure of the ratio of stable isotopes 13C:12C
      Comments             a character string with text providing additional relevant information for data
      =================   ==============
      --------
      Let's say you are interested in the samples 1, 160, and 300, and want to
      know more about the islands where they were observed:
      >>> from palmerpenguins import load_penguins_raw
      >>> penguins_raw = load_penguins_raw()
      >>> list(penguins_raw.iloc[[1, 160, 300],4])
      ['Torgersen', 'Biscoe', 'Dream']
      >>> dict(pd.value_counts(penguins_raw.Species))
      {'Adelie Penguin (Pygoscelis adeliae)': 152, 'Gentoo penguin (Pygoscelis papua)': 124, 'Chinstrap penguin (Pygoscelis antarctica)': 68}
      """
    stream = pkg_resources.resource_stream(__name__, 'data/penguins-raw.csv')
    penguins_raw = pd.read_csv(stream)
    return penguins_raw
