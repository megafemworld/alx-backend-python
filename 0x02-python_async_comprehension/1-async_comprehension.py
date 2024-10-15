#!/usr/bin/python3
"""
    1-async_comprehension.py
"""
import asyncio
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    return [gen async for gen in async_generator()]
