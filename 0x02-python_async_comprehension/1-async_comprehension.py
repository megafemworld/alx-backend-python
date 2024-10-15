#!/usr/bin/python3
"""
    1-async_comprehension.py
"""
import asyncio
from typing import List
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    return [gen async for gen in async_generator()]
