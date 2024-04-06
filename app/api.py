from flask import Flask, request, jsonify
from src.agents.coder.coder import Coder


app = Flask(__name__)

@app.route('/generate_code', methods=['POST'])
def generate_code():
    data = request.json
    step_by_step_plan = data.get('step_by_step_plan')
    user_context = data.get('user_context')
    search_results = data.get('search_results')
    project_name = data.get('project_name')
    base_model = data.get('base_model', 'default_model')  # Default model ID if not provided

    coder = Coder(base_model=base_model)
    try:
        valid_response = coder.execute(step_by_step_plan, user_context, search_results, project_name)
        return jsonify({'success': True, 'response': valid_response}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
