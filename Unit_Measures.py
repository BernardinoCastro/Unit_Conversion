units={
    'Length': {
        'Meter': 1,
        'Kilometer':1000,
        'Inch': 0.0254,
        'Mile': 1609.34,
        'Centimeter':0.01,
        'Millimeter': 0.001,
        'Yard':0.9144,
        'Foot':0.3048
    },
    'Mass':{
        'Kilogram'
    }




}
def convert_quantity(quantity,value,from_unit,to_unit):
    return(value * units[quantity][from_unit])/units[quantity][to_unit]

print(

)
