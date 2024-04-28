from flask import Blueprint, render_template, request

extrablue = Blueprint('extrablue', __name__)

@extrablue.route('/sorter', methods=['GET', 'POST'])
def sorter():
    if request.method == 'POST':
        helicopters_line = request.form.get('helicopters', '')  # Get input from form
        # Normalize input by splitting on newlines or spaces, and stripping extra whitespace
        helicopters = [h.strip() for h in helicopters_line.split() if h.strip()]
        # Format names to ensure they appear correctly in the template
        formatted_helicopters = ['"{}",'.format(helicopter) for helicopter in helicopters]
        return render_template('sorter.html', helicopters=formatted_helicopters)
    return render_template('sorter.html', helicopters=[])


@extrablue.route('/weapon-sorter', methods=['GET', 'POST'])
def weapon_sorter():
    categories = {}  # Initialize an empty dictionary for categories
    if request.method == 'POST':
        weapon_names = request.form.get('weapon_names', '')
        custom_categories = request.form.get('categories', '')

        # Initialize categories based on user input if available
        if custom_categories:
            categories = {category.strip(): [] for category in custom_categories.split(",") if category.strip()}
        else:
            # Default categories if user inputs none
            categories = {'arifle': [], 'optic': [], 'bipod': [], 'muzzle': [], 'srifle': []}

        weapon_array = weapon_names.split(", ")

        for weapon in weapon_array:
            added = False
            for category in categories:
                if category in weapon:
                    categories[category].append(f'"{weapon.strip()}",')
                    added = True
                    break
            if not added and custom_categories:  # If no category matched and custom categories are used
                categories.setdefault('others', []).append(f'"{weapon.strip()}",')

    return render_template('weapon_sorter.html', categories=categories)

