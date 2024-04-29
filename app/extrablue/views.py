from flask import Blueprint, render_template, request

extrablue = Blueprint('extrablue', __name__)

@extrablue.route('/sorter', methods=['GET', 'POST'])
def sorter():
    if request.method == 'POST':
        helicopters_line = request.form.get('helicopters', '')
        helicopters = [h.strip() for h in helicopters_line.split() if h.strip()]
        formatted_helicopters = ['"{}",'.format(helicopter) for helicopter in helicopters]
        return render_template('sorter.html', helicopters=formatted_helicopters)
    return render_template('sorter.html', helicopters=[])


@extrablue.route('/weapon-sorter', methods=['GET', 'POST'])
def weapon_sorter():
    categories = {}  # Initialize an empty dictionary for categories
    if request.method == 'POST':
        weapon_names = request.form.get('weapon_names', '').strip()
        custom_categories = request.form.get('categories', '').strip()

        if custom_categories:
            categories = {category.strip(): [] for category in custom_categories.split(",") if category.strip()}
        else:
            categories = {'arifle': [], 'optic': [], 'bipod': [], 'muzzle': [], 'srifle': []}

        weapon_array = [weapon.strip() for weapon in weapon_names.split(",")]

        for weapon in weapon_array:
            added = False
            for category in categories:
                if category in weapon:
                    categories[category].append(f'"{weapon}",')
                    added = True
                    break
            if not added and custom_categories: 
                categories.setdefault('others', []).append(f'"{weapon}"')

        # Debug print
    return render_template('weapon_sorter.html', categories=categories)
