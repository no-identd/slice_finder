from dataclasses import dataclass
from typing import Any


@dataclass
class Filter:
    """Filter object."""

    feature: str
    operator: str
    value: str | float | bool


@dataclass
class Extreme:
    """Extreme object."""

    data_metric_value: float
    filtered_data: Any
    filtered_data_metric_value: float
    filters: list[Filter]

    def get_prettified_view(self) -> str:
        """Replace the default behavior of `print`.

                Returns:
                    Prettified text."""
        
        textual_filters = [
            f'{filter.feature} {filter.operator} {filter.value}'
            for filter in self.filters
        ]
        textual_composite_filter = '\nAND '.join(textual_filters)
        return f"""When {textual_composite_filter},
the value of the metric on the filtered data is {self.filtered_data_metric_value}
compared to {self.data_metric_value} on the whole data.
"""

    def __str__(self) -> str:
         return self.get_prettified_view()
    
    def __repr__(self) -> str:
         return self.get_prettified_view()