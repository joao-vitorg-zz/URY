# -*- coding: utf-8 -*-
from scrapy import Selector, Field, Item
from scrapy.loader.processors import MapCompose, Join


def normalizer(text):
    return Selector(text=text).xpath('normalize-space(.)').extract()


def to_dict(array):
    return {array[n]: array[n + 1] for n in range(0, len(array), 2)}


class Problem(Item):
    title = Field(
        input_processor=MapCompose(normalizer),
        output_processor=Join(),
    )
    number = Field(
        output_processor=lambda x: x[0],
    )
    description = Field(
        input_processor=MapCompose(normalizer),
        output_processor=Join(),
    )
    input = Field(
        input_processor=MapCompose(normalizer),
        output_processor=Join(),
    )
    output = Field(
        input_processor=MapCompose(normalizer),
        output_processor=Join(),
    )
    examples = Field(
        input_processor=MapCompose(normalizer),
        output_processor=to_dict,
    )
