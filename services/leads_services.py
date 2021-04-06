import csv

class LeadsServices:

    @staticmethod
    def read_csv():
        with open ('leads.csv', 'r') as f:
            return [lead for lead in csv.DictReader(f)]

    @staticmethod
    def append_csv(lead):
        with open('leads.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'nome', 'telefone', 'email', 'profissao'])
            writer.writerow(lead)

    @staticmethod
    def register(json):
        leads = LeadsServices.read_csv()
        get_lead_by_email = [lead for lead in leads if lead['email'] == json['email']]

        if len(get_lead_by_email) == 0:
            id = 1

            if leads != []:
                id = int(leads[-1]['id']) + 1

                json['id'] = id

                LeadsServices.append_csv(json)

                return json

        return False