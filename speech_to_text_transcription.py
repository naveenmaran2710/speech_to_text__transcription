import speech_recognition as sr
import Levenshtein

def calculate_word_error_rate(hypothesis, reference):
    hypothesis = hypothesis.split()
    reference = reference.split()

    # Use Levenshtein distance to calculate WER
    wer = Levenshtein.distance(' '.join(hypothesis), ' '.join(reference))
    wer_rate = wer / len(reference) * 100

    return wer_rate

def evaluate_transcription_accuracy(audio_file, transcribed_text):
    # Replace this with the actual ground truth for evaluation
    ground_truth = "This is the ground truth text."

    wer_rate = calculate_word_error_rate(transcribed_text, ground_truth)

    print(f"Word Error Rate for '{audio_file}': {wer_rate:.2f}%")

def optimize_transcription_tool(input_audio_path, output_text_path):
    # Initialize the speech recognition object
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(input_audio_path) as source:
        audio = recognizer.record(source)

    try:
        # Use a speech recognition engine (e.g., Google Web Speech API)
        text = recognizer.recognize_google(audio, language="en-IN")  # Modify language code as needed

        # Evaluate transcription accuracy
        evaluate_transcription_accuracy(input_audio_path, text)

        # Save the transcribed text to an output file
        with open(output_text_path, 'w') as output_file:
            output_file.write(text)

        print("Transcription successful!")
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Web Speech API; {e}")

if __name__ == "__main__":
    # Example usage
    audio_file_path = "C:\\Users\\navee\\OneDrive\\Desktop\\Project Transcription\\Python tests\\English_Sample_Input(converted_audio_from_mp3 to wav format).wav"
    output_text_file_path = "C:\\Users\\navee\\OneDrive\\Desktop\\Project Transcription\\Python tests\\sample_output.txt"

    optimize_transcription_tool(audio_file_path, output_text_file_path)
