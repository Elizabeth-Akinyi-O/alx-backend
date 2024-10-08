#!/usr/bin/env python3

""" Deletion-resilient hypermedia pagination. """

import csv
import math
from typing import List, Dict


class Server:
    """ Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """ Dataset indexed by sorting position, starting at 0. """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """ Retrieves info about a page from a given index and with a
        specified size.
        """
        assert type(index) == int and index <= len(self.dataset())

        dataset = self.indexed_dataset()

        data = []
        count = 0
        for key, value in dataset.items():
            if key >= index and count < page_size:
                count += 1
                data.append(value)
                continue

            if count == page_size:
                next_index = key
                break

        # diff = len(self.dataset()) - len(self.indexed_dataset())
        # end_index = index + page_size + diff
        # for i in range(index, end_index):
        #     try:
        #         data.append(dataset[i])
        #     except KeyError:
        #         i += 1

        res = {
            "index": index if index else 0,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }

        return res
