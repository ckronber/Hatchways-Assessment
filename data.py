class testResult(unittest.TestCase):
    def compare_solutions(self):
        solution_url_split = ["https://api.hatchways.io/assessment/solution/","posts?tags=history,tech&sortBy=likes&direction=desc"]
        full_solution = self.solution_url_split[0]+ self.solution_url_split[1]
        sol_request = requests.get(full_solution).json()
        my_string:str = "http://localhost:5000/"+solution_url_split[1]
        solution =  requests.get(my_string).json()
        self.assertEqual(solution,sol_request)
