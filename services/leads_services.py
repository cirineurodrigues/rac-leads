import csv
class LeadsServices:

    @staticmethod
    def read_csv():
        with open ('leads.csv', 'r') as f:
            return [lead for lead in csv.DictReader(f)]

    @staticmethod
    def append_csv(lead):
        with open('leads.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=['nome', 'telefone', 'email', 'profissao'])
            writer.writerow(lead)

    @staticmethod
    def register(json):
        LeadsServices.append_csv(json)