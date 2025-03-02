import os
import PyPDF2

def merge_pdfs(pdf_list, output_filename):
    """Merge multiple PDFs into one."""
    merger = PyPDF2.PdfMerger()
    
    for pdf in pdf_list:
        try:
            merger.append(pdf)
        except Exception as e:
            print(f"Error merging {pdf}: {e}")
    
    merger.write(output_filename)
    merger.close()
    print(f"Merged PDF saved as: {output_filename}")

def split_pdf(pdf_path, output_folder):
    """Split a PDF into individual pages."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        with open(pdf_path, "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for i in range(len(reader.pages)):
                writer = PyPDF2.PdfWriter()
                writer.add_page(reader.pages[i])

                output_filename = os.path.join(output_folder, f"page_{i+1}.pdf")
                with open(output_filename, "wb") as output_pdf:
                    writer.write(output_pdf)
                
                print(f"Saved: {output_filename}")

    except Exception as e:
        print(f"Error splitting PDF: {e}")

def main():
    while True:
        print("\nPDF Merger & Splitter")
        print("1. Merge PDFs")
        print("2. Split PDF")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            pdf_list = input("Enter PDF file paths separated by commas: ").split(',')
            pdf_list = [pdf.strip() for pdf in pdf_list]
            output_filename = input("Enter output merged PDF filename: ")
            merge_pdfs(pdf_list, output_filename)

        elif choice == "2":
            pdf_path = input("Enter the PDF file path to split: ")
            output_folder = input("Enter the folder to save split pages: ")
            split_pdf(pdf_path, output_folder)

        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
