#!/usr/bin/python3
"""
    1-async_comprehension.py
"""
import asyncio
from typing import Generator
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    return [_ async for _ in async_generator()]
