import pandas


class DataFrameProcessing:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.read_data()

    def read_data(self):
        data = pandas.read_csv(self.filepath, index_col='PassengerId')
        return data

    def count_passengers_by_gender(self):
        return self.data['Sex'].value_counts()

    def calculate_survived_passengers(self):
        survived_passengers = len(self.data[self.data['Survived'] == 1])
        all_passengers = len(self.data)
        return "%.2f" % ((survived_passengers * 100) / all_passengers)

    def calculate_first_class_passengers_value(self):
        first_class_passengers = len(self.data[self.data['Pclass'] == 1])
        all_passengers = len(self.data)
        return "%.2f" % ((first_class_passengers * 100) / all_passengers)

    def calculate_mean_age(self):
        return "%.2f" % self.data['Age'].mean()

    def calculate_median_age(self):
        return "%.2f" % self.data['Age'].median()

    def calculate_pearson_correlation(self):
        siblings_series = pandas.Series(self.data['SibSp'])
        parch_series = pandas.Series(self.data['Parch'])
        return "%.2f" % siblings_series.corr(parch_series)

    def find_most_popular_name(self):
        names_and_sex = self.data['Name'] + ';' + self.data['Sex']
        names = []

        for name in names_and_sex:
            if name.split(';')[1] == 'female':
                if '(' in name.split(';')[0]:
                    splitted = name.split(';')[0].split('(')[-1].split(' ')[0]
                    names.append(splitted)
                else:
                    splitted_miss = name.split(';')[0].replace('Miss.', '').split(',')[1]
                    names.append(splitted_miss)

        series = pandas.Series(names)
        return series.value_counts()


if __name__ == '__main__':
    data_frame = DataFrameProcessing('titanic.csv')
    print('genders count', data_frame.count_passengers_by_gender())
    print('survived passengers', data_frame.calculate_survived_passengers())
    print('first class passengers', data_frame.calculate_first_class_passengers_value())
    print('mean and median age', data_frame.calculate_mean_age(), data_frame.calculate_median_age())
    print('correlation', data_frame.calculate_pearson_correlation())
    print('the most popular woman name ', data_frame.find_most_popular_name())
