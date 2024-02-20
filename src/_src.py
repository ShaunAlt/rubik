# =============================================================================
# Created By: Shaun Altmann
# =============================================================================
'''
Rubik's Cube Model Source Module
-
Contains constants, type definitions, functions, and base objects for the
Rubik's Cube Model.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for type hinting
from typing import (
    Any,
)


# =============================================================================
# Type Definitions
# =============================================================================
_COLOUR = tuple[int, str] | None
_COLOUR_PIECE_CUBE = tuple[
    tuple[_COLOUR, _COLOUR], # X Positive, X Negative
    tuple[_COLOUR, _COLOUR], # Y Positive, Y Negative
    tuple[_COLOUR, _COLOUR], # Z Positive, Z Negative
]
_DATA = dict[str, Any]
_POS = tuple[float, float, float]


# =============================================================================
# Constant Definitions
# =============================================================================


# ==========================
# Pre-Set Colour Definitions
class COLOURS():
    ''' Pre-Set Colour Definitions. '''

    # =======================
    # Cube Colour Definitions
    class CUBE():
        ''' Cube Colour Definitions. '''

        B = (2, 'B')
        G = (3, 'G')
        O = (4, 'O')
        R = (1, 'R')
        W = (0, 'W')
        Y = (5, 'Y')
        ALL = [B, G, O, R, W, Y]


# =============================================================================
# Generic Object Definition
# =============================================================================
class OBJ(object):
    '''
    Generic Object Definition
    -
    Contains the basic information that all objects in this module contain.

    Attributes
    -
    None

    Methods
    -
    - _get_data(short=False) : `_DATA`
        - Instance Method.
        - Gets all data from the current instance of the object.
    '''

    # ========
    # Get Data
    def _get_data(
            self,
            short: bool = False
    ) -> _DATA:
        '''
        Get Data
        -
        Gets all data from the current instance of the object.

        Parameters
        -
        - short : `bool`
            - Whether or not to return only the shortened version of the data.

        Returns
        -
        - `_DATA`
            - Object instance data.
        '''

        raise NotImplementedError(
            'OBJ._get_data() must be implemented in subclasses.'
        )
    
    # ===================
    # Long Representation
    def __repr__(self) -> str:
        '''
        Long Representation
        -
        Returns a string representation of the current instance of the object
        in a long (multi-line) representation.

        Parameters
        -
        None

        Returns
        -
        - `str`
            - Long string representation of the current instance of the object.
        '''

        cls_name: str = self.__class__.__name__
        output: str = f'<{cls_name}>'
        for key, val in self._get_data().items():
            val_str: str = str(val)
            if isinstance(val, list):
                val_str = (
                    '[' \
                    + (',\n\t\t'.join([str(sub_val) for sub_val in val])) \
                    + ']'
                )
            output += f'\n\t{key} = {val_str}'

        return output + f'\n</{cls_name}>'
    
    # ====================
    # Short Representation
    def __str__(self) -> str:
        '''
        Short Representation
        -
        Returns a string representation of the current instance of the object
        in a short (single-line) representation.

        Parameters
        -
        None

        Returns
        -
        - `str`
            - Short string representation of the current instance of the
                object.
        '''

        output: str = (
            f'<{self.__class__.__name__}' \
            + (
                ', '.join([
                    f'{key} = {val}' 
                    for key, val 
                    in self._get_data(True).items()
                ])
            ) \
            + ' />'
        )

        return output


# =============================================================================
# End of File
# =============================================================================
