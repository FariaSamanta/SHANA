import bz2

def main():
    input_file = "shape_predictor_68_face_landmarks.dat.bz2"
    output_file = "shape_predictor_68_face_landmarks.dat"

    # Extract the .bz2 file
    with bz2.BZ2File(input_file, "rb") as f:
        data = f.read()

    # Write the extracted data to a new file
    with open(output_file, "wb") as f:
        f.write(data)

    print("Extraction complete! The file is saved as:", output_file)

if __name__ == "__main__":
    main()

