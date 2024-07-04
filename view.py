from flask import Flask, render_template, request
import os

app = Flask(__name__)

grade_points = {
    'F': 0,
    'P': 4,
    'E': 5,
    'D': 6,
    'C': 7,
    'B': 8,
    'A': 9,
    'S': 10
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            num_semesters = int(request.form['num_semesters'])
            sgpa_list = []
            total_credits_list = []

            for sem in range(num_semesters):
                num_courses = int(request.form[f'num_courses_{sem}'])
                total_credits = 0.0
                total_grade_points = 0.0

                for course in range(num_courses):
                    grade = request.form[f'grade_{sem}_{course}']
                    credits = int(request.form[f'credits_{sem}_{course}'])
                    total_credits += credits
                    total_grade_points += grade_points[grade] * credits

                sgpa_list.append(total_grade_points / total_credits)
                total_credits_list.append(total_credits)

            total_quality_points = sum(sgpa * credits for sgpa, credits in zip(sgpa_list, total_credits_list))
            total_credits = sum(total_credits_list)
            cgpa = total_quality_points / total_credits

            return render_template('index.html', cgpa=round(cgpa, 2), sgpas=sgpa_list, num_semesters=num_semesters)

        except KeyError as e:
            return render_template('index.html', error=f"Missing input for {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT',5000))
    app.run(debug=True, host='0.0.0.0', port=port)
