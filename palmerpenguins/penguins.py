import pandas as pd
import importlib.resources
from typing import Union, overload, Literal, Tuple, cast


@overload
def load_penguins(
    return_X_y: Literal[False] = False, drop_na: bool = False
) -> pd.DataFrame: ...


@overload
def load_penguins(
    return_X_y: Literal[True], drop_na: bool = False
) -> Tuple[pd.DataFrame, pd.Series]: ...


def load_penguins(
    return_X_y: bool = False, drop_na: bool = False
) -> Union[pd.DataFrame, Tuple[pd.DataFrame, pd.Series]]:
    """Load and return the penguins dataset (classification).

    The Palmer penguins dataset is a dataset for data exploration & visualization, and can be used as an
    alternative to the Iris dataset.

    +-------------------+----------------------+
    | Classes           | 3                    |
    +-------------------+----------------------+
    | Samples per class | [152,168,124]        |
    +-------------------+----------------------+
    | Samples total     | 344                  |
    +-------------------+----------------------+
    | Dimensionality    | 8                    |
    +-------------------+----------------------+
    | Features          | real, integer,       |
    |                   | string, positive     |
    +-------------------+----------------------+

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
        A dataframe of shape (344, 8) and has the following columns:

        +-------------------+--------------------------------------------------------------------------+
        | Column            | Description                                                              |
        +===================+==========================================================================+
        | species           | A string denoting penguin species (Adélie, Chinstrap and Gentoo)        |
        +-------------------+--------------------------------------------------------------------------+
        | island            | A string denoting island in Palmer Archipelago, Antarctica (Biscoe,     |
        |                   | Dream or Torgersen)                                                      |
        +-------------------+--------------------------------------------------------------------------+
        | bill_length_mm    | A number denoting bill length (millimeters)                              |
        +-------------------+--------------------------------------------------------------------------+
        | bill_depth_mm     | A number denoting bill depth (millimeters)                               |
        +-------------------+--------------------------------------------------------------------------+
        | flipper_length_mm | An integer denoting flipper length (millimeters)                         |
        +-------------------+--------------------------------------------------------------------------+
        | body_mass_g       | An integer denoting body mass (grams)                                    |
        +-------------------+--------------------------------------------------------------------------+
        | sex               | A string denoting penguin sex (female, male)                             |
        +-------------------+--------------------------------------------------------------------------+
        | year              | An integer denoting the study year (2007, 2008, or 2009)                |
        +-------------------+--------------------------------------------------------------------------+

    (data, target) : tuple if ``return_X_y`` is True
        A tuple containing:

        data: DataFrame of shape (344, 4)
            Contains the four size measurements: bill_length_mm, bill_depth_mm,
            flipper_length_mm, and body_mass_g.

        target: Series of shape (344,)
            The classification target (penguin species).

    Examples
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
    with (
        importlib.resources.files(__package__)
        .joinpath("data/penguins.csv")
        .open("rb") as stream
    ):
        penguins = pd.read_csv(stream)

    if drop_na:
        penguins.dropna(inplace=True)

    if return_X_y:
        data = cast(
            pd.DataFrame,
            penguins[
                ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
            ],
        )
        target = cast(pd.Series, penguins["species"])

        return data, target

    return penguins


def load_penguins_raw() -> pd.DataFrame:
    """Load and return the raw penguins dataset (classification).

    Data were collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.

    It Includes all the variables and original names, nesting observations, penguin size data, and isotope measurements from blood samples for adult Adélie, Chinstrap, and Gentoo penguins.

    +-------------------+----------------------+
    | Classes           | 3                    |
    +-------------------+----------------------+
    | Samples per class | [152,168,124]        |
    +-------------------+----------------------+
    | Samples total     | 344                  |
    +-------------------+----------------------+
    | Dimensionality    | 17                   |
    +-------------------+----------------------+
    | Features          | real, integer,       |
    |                   | string, positive     |
    +-------------------+----------------------+

    Read more in the :ref:`https://github.com/allisonhorst/palmerpenguins`.

    Returns
    -------
    data : :class:`pandas.core.frame.DataFrame`
        A dataframe of shape (344  , 17) and has the following columns:

        +-------------------+-------------------------------------------------------------------------+
        | Column            | Description                                                             |
        +===================+=========================================================================+
        | studyName         | Sampling expedition from which data were collected, generated, etc.     |
        +-------------------+-------------------------------------------------------------------------+
        | Sample Number     | An integer denoting the continuous numbering sequence for each sample   |
        +-------------------+-------------------------------------------------------------------------+
        | Species           | A string denoting the penguin species                                   |
        +-------------------+-------------------------------------------------------------------------+
        | Region            | A string denoting the region of Palmer LTER sampling grid              |
        +-------------------+-------------------------------------------------------------------------+
        | Island            | A string denoting the island near Palmer Station where samples were    |
        |                   | collected                                                               |
        +-------------------+-------------------------------------------------------------------------+
        | Stage             | A character string denoting reproductive stage at sampling             |
        +-------------------+-------------------------------------------------------------------------+
        | Individual ID     | A string denoting the unique ID for each individual in dataset         |
        +-------------------+-------------------------------------------------------------------------+
        | Clutch Completion | A string denoting if the study nest observed with a full clutch,       |
        |                   | i.e., 2 eggs                                                            |
        +-------------------+-------------------------------------------------------------------------+
        | Date Egg          | A date denoting the date study nest observed with 1 egg (sampled)      |
        +-------------------+-------------------------------------------------------------------------+
        | Culmen Length     | A number denoting the length of the dorsal ridge of a bird's bill      |
        |                   | (millimeters)                                                           |
        +-------------------+-------------------------------------------------------------------------+
        | Culmen Depth      | A number denoting the depth of the dorsal ridge of a bird's bill       |
        |                   | (millimeters)                                                           |
        +-------------------+-------------------------------------------------------------------------+
        | Flipper Length    | An integer denoting the length penguin flipper (millimeters)           |
        +-------------------+-------------------------------------------------------------------------+
        | Body Mass         | An integer denoting the penguin body mass (grams)                       |
        +-------------------+-------------------------------------------------------------------------+
        | Sex               | A character string denoting the sex of an animal                        |
        +-------------------+-------------------------------------------------------------------------+
        | Delta 15 N        | A number denoting the measure of the ratio of stable isotopes 15N:14N  |
        +-------------------+-------------------------------------------------------------------------+
        | Delta 13 C        | A number denoting the measure of the ratio of stable isotopes 13C:12C  |
        +-------------------+-------------------------------------------------------------------------+
        | Comments          | A character string with text providing additional relevant information  |
        |                   | for data                                                                |
        +-------------------+-------------------------------------------------------------------------+

    Examples
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
    with (
        importlib.resources.files(__package__)
        .joinpath("data/penguins-raw.csv")
        .open("rb") as stream
    ):
        penguins_raw = pd.read_csv(stream)
    return penguins_raw
