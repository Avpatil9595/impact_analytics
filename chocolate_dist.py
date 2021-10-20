class ChocolateDistributionService:
    def __init__(self):
        self.num_of_test = self.__get_test_number()
        self.num_of_colleague = self.__get_colleague_number()
        self.colleagues_num_of_chocolates = self.__get_number_of_chocolates()

    @staticmethod
    def __get_test_number():
        return int(input("Enter Number of Tests"))

    @staticmethod
    def __get_colleague_number():
        return int(input("Enter Number of Colleague"))

    def __get_number_of_chocolates(self):
        chocolates = input(f"Enter Number of Chocolates of {self.num_of_colleague} Colleague")
        if len(chocolates.split()) < self.num_of_colleague:
            raise ValueError('Invalid Data')

        list_of_chocolates = [int(c) for c in chocolates.split()]
        return list_of_chocolates

    def get_number_of_operations(self):
        minimum_choc = min(self.colleagues_num_of_chocolates)
        number_of_operations = [0] * 4
        for num in self.colleagues_num_of_chocolates:
            for count in range(4):
                diff = num - (minimum_choc - count)
                c_sum = diff // 5 + (diff % 5) // 2 + (diff % 5) % 2
                number_of_operations[count] += c_sum
        return print(min(number_of_operations))


if __name__ == '__main__':
    ChocolateDistributionService().get_number_of_operations()
