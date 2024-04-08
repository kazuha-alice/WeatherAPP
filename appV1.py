# _Weather App_

import flet
from flet import *
import requests
import json
import datetime

APIKEY_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('API_KEY', 'r').read().strip()
CITY = 'Delhi'
url = APIKEY_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
#print(response)

days = [
    'Monday',
    'Tuesday',
    'Thursday',
    'Wednesday',
    'Friday',
    'Saturday',
    'Sunday'
]


def main(page: flet.Page):
    page.horizontal_alignment='center'
    page.vertical_alignment='center'


    def current_temperature():
        temp_kelvin = response['main']['temp']
        current_weather = response['weather'][0]['main']
        current_humidity = response['main']['humidity']
        current_weather_disceiption = response['weather'][0]['description']
        current_wind = response['wind']['speed']
        feels_like = response['main']['feels_like']
        current_feels_like = feels_like - 273.15
        celcius = temp_kelvin - 273.15
        return [
            celcius, 
            current_weather, 
            current_weather_disceiption,
            current_humidity,
            current_wind, 
            current_feels_like,
            ]
    
    def temperature_expand():
        temp_info =[]
        info = [
            [
                int(response['visibility']/1000),
                'km', 'Visibility', 
                'Lottie/IMG/visibility.png'
            ],
            [
                round(response['main']['pressure']*0.03,2),
                'inHg', 'Pressure', 
                'Lottie/IMG/pressure.png'
            ],
            [
                datetime.datetime.fromtimestamp(response['sys']['sunset']).strftime('%I:%M %p'),
                ' ', 'Sunset', 
                'Lottie/IMG/sunset.png'
            ],
            [
                datetime.datetime.fromtimestamp(response['sys']['sunrise']).strftime('%I:%M %p'),
                ' ', 'Sunrise', 
                'Lottie/IMG/sunrise.png'
            ]
        ]

        for data_info in info:
            temp_info.append(
                Container(
                    bgcolor='white10',
                    border_radius=15, alignment=alignment.center,
                    content=Column(
                        alignment='center',
                        horizontal_alignment='center',
                        spacing=25,
                        controls=[
                            Container(
                                alignment=alignment.center,
                                content=Image(
                                    src=data_info[3], color='white',
                                ), width=32, height=32,
                            ),
                            Container(
                                content=Column(
                                    alignment=alignment.center,
                                    horizontal_alignment='center',
                                    spacing=0,
                                    controls=[
                                        Text(
                                            str(data_info[0])+' '+data_info[1],
                                            size=12, color='white'
                                        ),
                                        Text(
                                            data_info[2],
                                            size=12, color='white54'
                                        )
                                    ]
                                )
                            )
                        ]
                    )
                )
            )
        return temp_info    
        


    
    

    def _expand(e):
        if e.data == 'true':
            _c.content.controls[0].height = 560
            _c.content.controls[0].update()
        else:
            _c.content.controls[0].height = 660*0.40
            _c.content.controls[0].update()
        

    def _top():

        today = current_temperature()
        today_temp = str(int(today[0]))
        #print(today)

        today_description = GridView(
            padding=10,
            max_extent=150, expand=1, 
            run_spacing=5,
            spacing=5,
        )
        for info_temp in temperature_expand():
            today_description.controls.append(info_temp)
            

        top = Container(
            width=310, height=660*0.40,
            gradient=LinearGradient(
                begin=alignment.bottom_left,
                end=alignment.top_right,
                colors=["purple300", "blue400"],
            ),
            border_radius=35,
            animate=animation.Animation(duration=420,
                                        curve="decelerate",),
                                        on_hover=lambda e: _expand(e),
                                        content=Column(
                                            alignment='start',
                                            spacing=10,
                                            controls=[
                                                Row(
                                                    alignment='center', 
                                                    spacing=20,
                                                    controls=[
                                                        Text('Delhi, IN',
                                                             size=16, weight='w600',
                                                             color='onprimary')
                                                    ],
                                                ),
                                                Container(padding=padding.only(bottom=5)),
                                                Row(alignment='center',
                                                    spacing=30,
                                                    controls=[
                                                        Column(controls=[
                                                            Container(
                                                                width=90, height=90,
                                                                image_src='Lottie/IMG/Weather_1.png'
                                                            )
                                                        ],),
                                                        Column(
                                                            horizontal_alignment='center',
                                                            spacing=5,
                                                            controls=[
                                                                Text(
                                                                    'Today\'s Weather',
                                                                    size=14, text_align='center', 
                                                                    color='onprimary', weight='w500',                                                                
                                                                
                                                                ),
                                                                Row(
                                                                    vertical_alignment='center',
                                                                    spacing=0, controls=[
                                                                        Container(
                                                                            content=Text(
                                                                                today_temp, size=32,
                                                                                weight='w600', color='onprimary'
                                                                            ),
                                                                        ), 
                                                                        Container(
                                                                            content=Text(
                                                                                '°C',size=32,weight='w600', 
                                                                                color='onprimary', 
                                                                            )
                                                                        )
                                                                    ]
                                                                ),
                                                                Text(
                                                                    today[1] + ' - Overcast', size=12,
                                                                    color='white54', text_align='center'
                                                                ),
                                                            ],

                                                        ),
                                                    ],),Divider(
                                                        height=8, thickness=1, color='white54'
                                                    ), Row(
                                                        alignment='spaceAround', controls=[
                                                            Container(
                                                                content=Column(
                                                                    horizontal_alignment='center',
                                                                    spacing=3, controls=[
                                                                        Container(
                                                                            alignment=alignment.center,
                                                                            content=Image(src='Lottie/IMG/wind.png', color='white'),
                                                                            width=20,height=20,
                                                                        ), Text(
                                                                            str(today[4]) + ' km/h', 
                                                                            size=12, color='white',
                                                                        ), Text(
                                                                            'Wind', size=10, color='white54',
                                                                        )
                                                                    ]
                                                                )
                                                            ), Container(
                                                                content=Column(
                                                                    horizontal_alignment='center',
                                                                    spacing=3, controls=[
                                                                        Container(
                                                                            alignment=alignment.center,
                                                                            content=Image(src='Lottie/IMG/humidity.png', color='white'),
                                                                            width=20,height=20,
                                                                        ), Text(
                                                                            str(today[3]) + '%', 
                                                                            size=12, color='white',
                                                                        ), Text(
                                                                            'Humidity', size=10, color='white54',
                                                                        )
                                                                    ]
                                                                )
                                                            ),Container(
                                                                content=Column(
                                                                    horizontal_alignment='center',
                                                                    spacing=3, controls=[
                                                                        Container(
                                                                            alignment=alignment.center,
                                                                            content=Image(src='Lottie/IMG/thermometer.png', color='white'),
                                                                            width=20,height=20,
                                                                        ), Text(
                                                                            str(int(today[5])) + '°C', 
                                                                            size=12, color='white',
                                                                        ), Text(
                                                                            'Feel\'s Like', size=10, color='white54',
                                                                        )
                                                                    ]
                                                                )
                                                            ),
                                                        ]
                                                    ), today_description, #GRID VIEW

                                            ]
                                        )
        )
        return top
    

    _c = Container(
        width=310,
        height=660,
        border_radius=35,
        bgcolor='#000000',
        padding=10,
        content=Stack(
            width=300,
            height=550,
            controls=[_top(),
                      ],
        )

    )

    page.add(_c)


if __name__ == "__main__":
    flet.app(target=main)
