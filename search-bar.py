import flet
from flet import*

def main(page: flet.Page):

    def change_city():
        pass

    def city_country():
        pass

    resultSearch=Container(
        visible=False,
        content=Column([
            Text('result location', weight='bold'), Column()
        ])
    )
    page.window_width = 300
    #page.window_height = 200
    bar_search = flet.SearchBar(
        view_elevation=2,
        bar_bgcolor=flet.LinearGradient(
            begin=flet.alignment.top_right,
            end=flet.alignment.top_left,
            colors=['blue50', 'indigo50']
        ),
        bar_overlay_color='white',
        bar_hint_text='Country/City',
        view_hint_text='Search Place...',
        bar_leading=IconButton(icon='place'),
        bar_trailing=[Text(' ')],
        on_change=change_city,
        on_submit=city_country,
        full_screen=True,
        view_trailing=[
            FloatingActionButton(icon='favorite', bgcolor='indigo')
        ],


    )
    page.add(
        Column([
            bar_search,
            resultSearch
        ])
    )

flet.app(target=main, view=AppView.WEB_BROWSER)