"""
Module Containing classes and functions modelling a simplified
Electricity Market.

"""

from datetime import datetime, timedelta
import math
import random


def get_demand(time: datetime):
    """
    Returns the demand for electricity at a given time.

    Parameters
    ----------
    time : datetime
        The time for which the demand is required.

    Returns
    -------
    demand : float
        The demand for electricity in MW at the given time.

    """

    return 35 + \
        7 * math.sin(2 * math.pi * ((time.hour + time.minute/60) - 9) / 24) \
        + 4.5 * math.sin(2 * math.pi * (time.month + time.day/30 - 1) / 12)


class Generator():
    """
    Class representing a generator in the electricity market.
    """

    def __init__(self, name:str, capacity:float, type:str, fuel_cost:float, OM_cost:float):
        """
        Parameters
        ----------
        name : str
            The name of the generator.
        capacity : float
            The maximum capacity of the generator in MW.
        type : str
            The type of generator. Can be 'coal', 'gas', 'nuclear', 'hydro', 'wind', 'solar', 'geothermal'.
        fuel_cost : float
            The fuel cost of generating electricity in $/MWh.
        OM_cost : float
            The operation and maintenance cost of generating electricity in $/MWh.

        """
    
        # Class variables
        self.name = name
        self.capacity = capacity
        self.type = type
        self.fuel_cost = fuel_cost
        self.OM_cost = OM_cost
    

        # Other helper variables
        self.revenue = 0        # $
        self.generated = 0      # MWh



    def bid(self, time):
        """
        Returns the bid of the generator at a given time.

        Parameters
        ----------
        time : datetime
            The time for which the bid is required.

        Returns
        -------
        capacity : float
            The capacity of the generator in MW at the given time.
        bid : float
            The bid of the generator in $/MWh at the given time.

        """

        return (0, 0)
    
    def dispatch(self, amount, price):
        """
        Dispatches the generator for a given amount at a given price.

        Parameters
        ----------
        amount : float
            The amount of electricity to be generated in MWh.
        price : float
            The price at which the electricity is to be generated in $/MWh.

        Returns
        -------
        capacity : float
            The capacity dispatched of the generator in MW at the given time.
        """

        return 0

    def __lt__(self, other):
        """
        Compares two generators based on their operating cost.
        """
        if isinstance(other, Generator):
            return (self.fuel_cost + self.OM_cost) < (other.fuel_cost + other.OM_cost)
        else:
            return NotImplemented



class Solar(Generator):
    """
    Class representing a solar generator in the electricity market.
    """
    
    def __init__(self, name:str, capacity:float):
        """
        Parameters
        ----------
        name : str
            The name of the generator.
        capacity : float
            The maximum capacity of the generator in MW.

        """
    
        super().__init__(name, capacity, 'solar', 0, 0.5)

    def bid(self, time):
        """
        Returns the bid of the generator at a given time.

        Parameters
        ----------
        time : datetime
            The time for which the bid is required.

        Returns
        -------
        capacity : float
            The capacity of the generator in MW at the given time.
        bid : float
            The bid of the generator in $/MWh at the given time.

        """

        # Calculate Current capacity
        capacity = random.random() * ((0.5 * self.capacity) + \
             (0.5 * self.capacity ) * math.sin(2 * math.pi * (time.hour + time.minute/60 - 6) / 24))
        
        # Set available capacity
        self.available_capacity = capacity

        # Return capacity and bid
        return (capacity, self.OM_cost)