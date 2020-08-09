import os
import pandas as pd
import numpy as np


def load_penguins( return_X_y=False):
    """Load and return the penguins dataset (classification).

      The Palmer penguins dataset is a dataset for data exploration & visualization, and can be used as an
      alternative to the Iris dataset
      =================   ==============
      Classes                          3
      Samples per class        [152,168,124]
      Samples total                  334
      Dimensionality                  8
      Features            real, integer, string, positive
      =================   ==============


      Columns
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

      Read more in the :ref:`User Guide <wine_dataset>`.
      Parameters
      ----------
      return_X_y : bool, default=False
          If True, returns a ``(data, target)`` tuple instead of a dataframe object.
          See below for more information about the `data` and `target` object.

      Returns
      -------
      data : :class:`pandas.core.frame.DataFrame`
          data : a dataframe of shape (344  , 8)
          DESCR: str
              The full description of the dataset.
      (data, target) : tuple if ``return_X_y`` is True
          data : a dataframe of shape (344  , 4)   where each column corresponds to measurements
          target: {ndarray, Series} of shape (178,)
              The classification target. If `as_frame=True`, `target` will be
              a pandas Series.3
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
    penguins = pd.read_csv('data/penguins.csv')
    if return_X_y:
        data = penguins[['bill_length_mm', 'bill_depth_mm',
                        'flipper_length_mm', 'body_mass_g']]
        target = penguins['species']
        return data, target


    return penguins



def load_penguins_raw( return_X_y=False):
    """Load and return the penguins dataset (classification).

      The Palmer penguins dataset is a dataset for data exploration & visualization, and can be used as an
      alternative to the Iris dataset
      =================   ==============
      Classes                          3
      Samples per class        [152,168,124]
      Samples total                  334
      Dimensionality                  8
      Features            real, integer, string, positive
      =================   ==============


      Columns
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

      Read more in the :ref:`User Guide <wine_dataset>`.
      Parameters
      ----------
      return_X_y : bool, default=False
          If True, returns a ``(data, target)`` tuple instead of a dataframe object.
          See below for more information about the `data` and `target` object.

      Returns
      -------
      data : :class:`pandas.core.frame.DataFrame`
          data : a dataframe of shape (344  , 8)
          DESCR: str
              The full description of the dataset.
      (data, target) : tuple if ``return_X_y`` is True
          data : a dataframe of shape (344  , 4)   where each column corresponds to measurements
          target: {ndarray, Series} of shape (178,)
              The classification target. If `as_frame=True`, `target` will be
              a pandas Series.3
      --------
      Let's say you are interested in the samples 10, 80, and 140, and want to
      know their class name.
      >>> from palmerpenguins.penguins import load_penguins_raw
      >>> penguins = load_penguins()
      >>> list(penguins.iloc[[1, 160, 300],0])
      ['Adelie', 'Gentoo', 'Chinstrap']
      >>> dict(pd.value_counts(penguins.species))
      {'Adelie': 152, 'Gentoo': 124, 'Chinstrap': 68}
      """
    penguins = pd.read_csv('data/penguins.csv')
    if return_X_y:
        data = penguins[['bill_length_mm', 'bill_depth_mm',
                        'flipper_length_mm', 'body_mass_g']]
        target = penguins['species']
        return data, target


    return penguins