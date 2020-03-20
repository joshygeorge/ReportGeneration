from fpdf import FPDF
import json
import sys

class CustomPDF(FPDF):

    def __init__(self, json_path):
        FPDF.__init__(self)
        with open(json_path) as f:
            self.data = json.load(f)
    
    def header(self):
        # Set up a logo
        self.image('Jax.png', 10, 8, 33)
        self.set_font('Arial', '', 8)
        
        # Add an address
        self.set_text_color(128, 128, 128)
        self.cell(50)
        self.cell(19, 3, 'Patient Name: ')
        self.set_text_color(0, 0, 0)
        self.cell(13, 3, self.data["Patient Name"])
        self.cell(18)

        self.set_text_color(128, 128, 128)
        self.cell(7, 3, 'Test: ')
        self.set_text_color(0, 0, 0)
        self.cell(40, 3, self.data["Test"], 0, 1)

        self.cell(50)
        self.set_text_color(128, 128, 128)
        self.cell(15, 3, u'Patient ID: ')
        self.set_text_color(0, 0, 0)
        self.cell(30, 3, self.data["Patient ID"])
        self.cell(5)

        self.set_text_color(128, 128, 128)
        self.cell(17, 3, 'Report Date: ')
        self.set_text_color(0, 0, 0)
        self.cell(20, 3, self.data["Report Date"], 0, 1)
        
        # Line break
        self.ln(20)
        
    def footer(self):
        self.set_y(-15)
        self.set_x(10)
        
        self.set_font('Arial', 'I', 8)

        self.cell(30, 5, 'CLIA# 07D2061461')
        self.cell(20)
        self.cell(10, 5, u'CL-0695')
        self.cell(15)
        self.cell(0, 5, 'The Jackson Laboratory for Genomic Medicine, 10 Discovery Drive, Farmington, CT 06032', 0, 1)

        self.cell(65, 5, 'Lei Li, M.D., Ph.D., ABMGG, Clinical Laboratory Director')
        self.cell(10)
        self.cell(20, 5, 'Phone: 860 837 2320')
        self.cell(10)
        self.cell(20, 5, 'Fax: 860 856 2380')
        self.cell(50)
        self.cell(0, 5 , 'Page ' + str(self.page_no()) + '/{nb}')
        
def create_pdf(json_path):

    pdf = CustomPDF(json_path)
    # Create the special value {nb}
    pdf.alias_nb_pages()
    pdf.add_page()

    pdf.set_font('Times', '', 10)
    pdf.set_text_color(49, 85, 148)
    
    pdf.cell(40, 5, 'PATIENT')
    pdf.cell(20)
    pdf.cell(40, 5, 'SPECIMEN')
    pdf.cell(20)
    pdf.cell(40, 5, 'PHYSICIAN', 0, 1)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(10, 5, 'Name: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(30, 5, pdf.data["Patient Name"])
    pdf.cell(80)
    
    pdf.set_text_color(128, 128, 128)
    pdf.cell(10, 5, 'Name: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(30, 5, pdf.data["Physician Name"], 0, 1)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(16, 5, 'Patient ID: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(24, 5, pdf.data["Patient ID"])
    pdf.cell(20)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(20, 5, 'Specimen ID: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(20, 5, pdf.data["Specimen ID"])
    pdf.cell(20)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(17, 5, 'Affiliation: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(23, 5, pdf.data["Affiliation"], 0, 1)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(27, 5, 'Source Patient ID: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(13, 5, pdf.data["Source Patient ID"])
    pdf.cell(20)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(24, 5, 'Specimen Type: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(16, 5, pdf.data["Specimen Type"])
    pdf.cell(20)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(10, 5, 'Email: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(30, 5, pdf.data["Email"], 0, 1)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(11, 5, 'D.O.B: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(29, 5, pdf.data["D.O.B."])
    pdf.cell(20)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(22, 5, 'Received Date: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(18, 5, pdf.data["Recieved Date"])
    pdf.cell(20)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(11, 5, 'Phone: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(29, 5, pdf.data["Phone"], 0, 1)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(12, 5, 'Gender: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(28, 5, pdf.data["Gender"])
    pdf.cell(20)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(22, 5, 'Received time: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(18, 5, pdf.data["Recieved Time"])
    pdf.cell(20)

    pdf.set_text_color(128, 128, 128)
    pdf.cell(24, 5, 'Collection Date: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(16, 5, pdf.data["Collection Date"], 0, 1)

    pdf.cell(120)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(25, 5, 'Collection Time: ')
    pdf.set_text_color(0, 0, 0)
    pdf.cell(15, 5, pdf.data["Collection Time"], 0, 1)
    pdf.ln()

    pdf.set_font('Times', '', 18)
    pdf.set_text_color(49, 85, 148)
    pdf.cell(0, 10, u'JAX COVID-19 RT-PCR Assay', 0, 1, 'C')

    pdf.set_fill_color(34, 78, 119)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Times', '', 12)
    pdf.cell(80)
    pdf.cell(80, 10, 'Result', 0, 1, 'C', 1)
    pdf.cell(20)
    pdf.cell(60, 10, 'JAX COVID 19', 0, 0, 'C', 1)

    pdf.set_text_color(0, 0, 0)
    pdf.set_fill_color(242, 242, 242)
    pdf.cell(80, 10, pdf.data["Result"], 0, 1, 'C', 1)
    
    pdf.set_font('Times', '', 8)
    pdf.cell(20)
    pdf.cell(140, 5, u'Note: Please refer to "Test Interpretation" under "Methodology" for detailed information on interpretation of the results.', 0, 1)
    pdf.ln(20)

    pdf.set_font('Times', '', 18)
    pdf.set_text_color(49, 85, 148)
    pdf.cell(40, 10, 'TEST METHODS', 0, 1)
    
    pdf.set_font('Times', 'B', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(20, 5, 'Test Description', 0, 1)

    pdf.set_font('Times', '', 10)
    pdf.multi_cell(0, 5, u'The JAX COVID-19 RT-PCR Assay is Real Time Reverse Transcription Polymerase Chain Reaction (rRT-PCR) for the in vitro qualitative detection of three SARS-Cov-2 target sequences unique to the 2019-Novel Coronavirus (2019-nCoV). This testing requires respiratory samples such as nasopharyngeal swab, nasopharyngeal aspirate, and bronchoalveolar lavage. Purified RNA is reverse transcribed into cDNA and amplified using the TaqPath RT-PCR COVID-19 Kit on the Applied Biosystems 7500 Fast Dx Real-Time PCR instrument. In this process, specific primers and probes anneal to specific sequences of the SARS-CoV-2 located on the following genes: ORF1ab, N Protein and S Protein.')
    pdf.ln(10)

    pdf.set_font('Times', 'B', 10)
    pdf.cell(40, 5, 'Test Interpretation', 0, 1)

    pdf.set_font('Times', '', 10)
    pdf.multi_cell(0, 5, u'Data analysis and interpretation is performed using C q or C t values obtained from Design and Analysis Software v2.3. A total of two positive controls and one negative control are processed with each run and the validation of each run is determined on their performance. Reference interval for this testing is "Not Detected."')
    pdf.ln()

    pdf.set_font('Times', 'B', 10)
    pdf.cell(33, 5, 'Results Not Detected: ')
    pdf.set_font('Times', '', 10)
    pdf.cell(0, 5, u'negative for SARS-CoV-2. Recommend to test for other viruses if clinically indicated. Report results to', 0, 1)
    pdf.cell(20, 5, 'healthcare provider.', 0, 1)

    pdf.set_font('Times', 'B', 10)
    pdf.cell(27, 5, 'Results Detected: ')
    pdf.set_font('Times', '', 10)
    pdf.cell(0, 5, u'positive for SARS-CoV-2. Report results to healthcare provider and public health authorities.', 0, 1)

    pdf.set_font('Times', 'B', 10)
    pdf.cell(33, 5, 'Results Inconclusive: ')
    pdf.set_font('Times', '', 10)
    pdf.cell(0, 5, 'additional testing should be performed if clinically indicated.', 0, 1)

    pdf.set_font('Times', 'B', 10)
    pdf.cell(23, 5, 'Results Failed: ')
    pdf.set_font('Times', '', 10)
    pdf.cell(0, 5, 'additional specimen should be collected.', 0, 1)

    pdf.set_font('Times', 'B', 10)
    pdf.cell(28, 5, 'Results Canceled: ')
    pdf.set_font('Times', '', 10)
    pdf.cell(0, 5, 'sample did not meet acceptance criteria. Additional specimen should be collected.', 0, 1)
    
    pdf.add_page()
    pdf.set_font('Times', '', 18)

    pdf.set_text_color(49, 85, 148)
    pdf.cell(20, 5, 'LIMITATIONS', 0, 1)
    pdf.ln()

    pdf.set_font('Times', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 5, u'Positive results are indicative of the presence of SARS-CoV-2 RNA; clinical correlation with patient history and other diagnostic information is necessary to determine patient infection status. Positive results do not rule out bacterial infection or co-infection with other viruses. The agent detected may not be the definite cause of disease.')
    pdf.ln()

    pdf.multi_cell(0, 5, 'Negative results do not exclude SARS-CoV-2 infection and should not be used as the sole basis for patient management decisions. Negative results must be combined with clinical observations, patient history, and epidemiological information.')    
    pdf.ln()

    pdf.cell(0, 5, 'Improper sample collection, transport or storage may impede the ability of the assay to detect target sequences.')
    pdf.ln()

    pdf.multi_cell(0, 5, 'False negative results may be a result of improper sample collection and handling, which can cause degradation of the viral RNA during shipping/storage, presence of RT-PCR inhibitors, mutation in the SARS-CoV-2 virus, failure to follow instructions for this testing.')
    pdf.ln()

    pdf.multi_cell(0, 5, 'False positive may be a result of cross contamination during specimen handling and preparation, specimen mix-up, and other source of RNA contamination.')
    pdf.ln(20)

    pdf.set_font('Times', '', 18)
    pdf.set_text_color(49, 85, 148)
    pdf.cell(20, 5, 'DISCLAIMER', 0, 1)
    pdf.ln()

    pdf.set_font('Times', '', 10)
    pdf.set_text_color(0, 0, 0)

    pdf.multi_cell(0, 5, 'Laboratories within the United States and its territories are required to report all positive results to the appropriate public health authorities.')
    pdf.ln()

    pdf.multi_cell(0, 5, u'This test has been developed and its analytical performance characteristics have been determined by The Jackson Laboratory. It has not been cleared or approved by the U.S. Food and Drug Administration (FDA). This test may be used for clinical purposes and should not be regarded as purely investigational or for research use only. This laboratory is certified under the Clinical Laboratory Improvement Amendments of 1988 (CLIA-88) as qualified to perform high complexity clinical testing.')
    pdf.ln(10)

    pdf.set_font('Times', '', 18)
    pdf.set_text_color(49, 85, 148)
    pdf.cell(5)
    pdf.cell(20, 5, 'REFERENCES', 0, 1)
    pdf.ln()

    pdf.set_font('Times', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(10)
    pdf.cell(100, 5, '1. TaqMan 2019 nCoV Assay Kit v2, Product Information Sheet [Applied Biosystems. (March 2020)].')
    pdf.ln(20)

    pdf.set_font('Times', 'B', 12)
    pdf.cell(5)
    pdf.cell(60, 5, 'Name: ________________________________')
    pdf.cell(30)
    pdf.cell(60, 5, 'Date: ________________________', 0, 1)
    
    pdf.set_font('Times', '', 10)
    pdf.cell(15)
    pdf.cell(20, 5, 'Lei Li, MD, PHD', 0, 1)

    pdf.cell(15)
    pdf.cell(20, 5, 'Clinical Laboratory Director', 0, 1)

    name = pdf.data["Patient Name"].replace(' ', "_")
    pdf.output(f'{name}_{pdf.data["Patient ID"]}_report.pdf')

if __name__ == '__main__':
    create_pdf(sys.argv[1])

