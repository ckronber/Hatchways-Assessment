import unittest,requests

class testResult(unittest.TestCase):
    def __init__(self):
        solution_url_split = ["https://api.hatchways.io/assessment/solution/","posts?tags=history,tech&sortBy=likes&direction=desc"]
        full_solution = solution_url_split[0]+ solution_url_split[1]
        self.sol_request = requests.get(full_solution).json()
        my_string:str = "http://localhost:5000/"+solution_url_split[1]
        self.solution = requests.get(my_string).json()

    async def compare_solutions(self):
        return self.assertEqual(self.solution,self.sol_request)
