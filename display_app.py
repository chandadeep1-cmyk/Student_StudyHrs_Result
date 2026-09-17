import gradio as gr
import pickle

# Load model
model = pickle.load(open("student_model.pkl", "rb"))

# Prediction function
def predict(hours):
    prediction = model.predict([[hours]])
    
    if prediction[0] == 1:
        return "PASS ✅"
    else:
        return "FAIL ❌"

# Create Gradio app
app = gr.Interface(
    fn=predict,
    inputs="number",
    outputs="text",
    title="Study Hours - Pass/Fail Predictor"
)

app.launch(server_name="0.0.0.0", server_port=7860)
