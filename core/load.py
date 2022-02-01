class Load:
    @staticmethod
    def add_rows_to_csv(rows):
        with open('data/collected_data.csv', 'a') as collected_data:
            collected_data.write('\n'.join([','.join(row) for row in rows]) + '\n')
