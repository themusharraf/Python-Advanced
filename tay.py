from typing import List, Dict, Union, Optional


def process_data(data: List[Dict[str, Union[int, float]]]) -> Optional[float]:
    if not data:
        return None
    return sum(item['value'] for item in data) / len(data)
