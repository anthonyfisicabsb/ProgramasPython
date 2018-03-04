from pygal.maps.world import World

wm = World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 30934000, 'mx': 113423000})

wm.render_to_file('no_populations.svg')
