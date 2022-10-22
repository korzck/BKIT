goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green', 'amount': 256},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black', 'amount':102},
   {'title': 'Стол маленький', 'price': 2700, 'color': 'white', 'amount': 53},
   {'title': 'Ваза для цветов', 'price': 1590, 'color': 'blue', 'amount': 96},
]

def field(items, *args):
    try:
        assert len(args) > 0
        r = [{} for i in range(len(items))]
        for i in range(len(items)):
            for key in items[i]:
                if key in args:
                    r[i].update({key:items[i][key]})
        return r
    except:
        print("Not list of dicts as argument passed")
