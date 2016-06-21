# Andelabs
Misc Andelabs exercises that fail to submit on labs.andela.com

# Binary Search Lab
Two of the tests fail and appear unpassable

On test_medium_list_search, we have:

```python
self.assertEqual(
            0,
            search2['count'],
            msg='should return {count: 0, index: 19} for 40'
        )
self.assertEqual(
            19,
            search2['index'],
            msg='should return {count: 5, index: 19} for 40'
        )
```

which apparently expects the search to find a value while looping 0 times. The code I have does 5 iterations, as shown on the second assert 'msg'

On test_large_list_search, we have:

```python
self.assertGreater(
            7,
            search3['count'],
            msg='should return {count: 3, index: -1} for 10000'
        )
```

which expects the search to complete a full search (full because it doesn't find the value) in less than 7 iterations. This seems impossible as the list has 100 items and we know binary search takes at worst case log2N iterations. Log2100 = 6.64 meaning we cannot complete a full search in less than 7 (6) iterations.

# Car Class Lab
On this lab my code passes all the tests but will not submit. The code fails some hidden tests. It is hard to even try to figure out which hidden tests these are since the lab did not provide a problem definition. Instead, it requires us figure out what to do from the tests. The tests only give a vague idea of what is supposed to happen, especially with regards to the drive(n) function.
