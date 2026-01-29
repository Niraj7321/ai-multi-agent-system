"""
Create Sample Competitive Exams
STET, CTET, BPSC, SSC, UPSC and more with real-style questions
"""
import sys
import io

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from src.competitive_exam_manager import CompetitiveExamManager

def create_stet_exam():
    """Create STET (State Teacher Eligibility Test) exam"""
    manager = CompetitiveExamManager()

    print("Creating STET 2024 Exam...")

    sections = [
        {
            "section_name": "Child Development and Pedagogy",
            "questions": [
                {
                    "question_id": "stet_cdp_1",
                    "question": "According to Piaget's theory, children in the concrete operational stage (7-11 years) can:",
                    "options": [
                        "Think abstractly about hypothetical situations",
                        "Understand conservation and reversibility",
                        "Only think about what they can see",
                        "Use symbolic thought but not logic"
                    ],
                    "correct_answer": 1,
                    "explanation": "Concrete operational stage children can perform mental operations on concrete objects, including understanding conservation.",
                    "marks": 1
                },
                {
                    "question_id": "stet_cdp_2",
                    "question": "Which of the following is NOT a principle of progressive education?",
                    "options": [
                        "Learning by doing",
                        "Child-centered approach",
                        "Rote memorization",
                        "Problem-solving approach"
                    ],
                    "correct_answer": 2,
                    "explanation": "Progressive education emphasizes active learning, not rote memorization.",
                    "marks": 1
                },
                {
                    "question_id": "stet_cdp_3",
                    "question": "Intrinsic motivation refers to:",
                    "options": [
                        "Motivation driven by external rewards",
                        "Motivation from within, driven by personal interest",
                        "Motivation from peer pressure",
                        "Motivation from fear of punishment"
                    ],
                    "correct_answer": 1,
                    "explanation": "Intrinsic motivation comes from internal satisfaction and personal interest.",
                    "marks": 1
                }
            ]
        },
        {
            "section_name": "Mathematics and Science",
            "questions": [
                {
                    "question_id": "stet_math_1",
                    "question": "If 20% of a number is 50, what is 35% of that number?",
                    "options": [
                        "75",
                        "87.5",
                        "90",
                        "100"
                    ],
                    "correct_answer": 1,
                    "explanation": "20% = 50, so 100% = 250. Therefore, 35% of 250 = 87.5",
                    "marks": 1
                },
                {
                    "question_id": "stet_sci_1",
                    "question": "Photosynthesis primarily occurs in which part of the plant?",
                    "options": [
                        "Roots",
                        "Stem",
                        "Leaves",
                        "Flowers"
                    ],
                    "correct_answer": 2,
                    "explanation": "Leaves contain chlorophyll which is essential for photosynthesis.",
                    "marks": 1
                }
            ]
        }
    ]

    exam = manager.create_exam(
        exam_name="STET 2024 - Paper 1",
        exam_type="STET",
        description="State Teacher Eligibility Test for Classes 1-5",
        sections=sections,
        duration_minutes=150,
        total_marks=150,
        passing_marks=90,
        negative_marking=0.25,
        difficulty="medium",
        tags=["2024", "Primary Teacher", "TET"]
    )

    print(f"✅ STET Exam Created: {exam['exam_id']}\n")
    return exam

def create_ctet_exam():
    """Create CTET (Central Teacher Eligibility Test) exam"""
    manager = CompetitiveExamManager()

    print("Creating CTET 2024 Exam...")

    sections = [
        {
            "section_name": "Child Development and Pedagogy",
            "questions": [
                {
                    "question_id": "ctet_cdp_1",
                    "question": "Which theory emphasizes the role of social interaction in cognitive development?",
                    "options": [
                        "Piaget's Cognitive Theory",
                        "Vygotsky's Sociocultural Theory",
                        "Bandura's Social Learning Theory",
                        "Skinner's Behaviorism"
                    ],
                    "correct_answer": 1,
                    "explanation": "Vygotsky emphasized that social interaction plays a fundamental role in cognitive development.",
                    "marks": 1
                },
                {
                    "question_id": "ctet_cdp_2",
                    "question": "The concept of 'Zone of Proximal Development' was given by:",
                    "options": [
                        "Jean Piaget",
                        "Lev Vygotsky",
                        "Jerome Bruner",
                        "Howard Gardner"
                    ],
                    "correct_answer": 1,
                    "explanation": "Vygotsky introduced the concept of ZPD - the difference between what a learner can do with and without help.",
                    "marks": 1
                }
            ]
        },
        {
            "section_name": "Language - English",
            "questions": [
                {
                    "question_id": "ctet_eng_1",
                    "question": "Choose the correct passive voice: 'She writes a letter.'",
                    "options": [
                        "A letter is written by her.",
                        "A letter was written by her.",
                        "A letter has been written by her.",
                        "A letter is being written by her."
                    ],
                    "correct_answer": 0,
                    "explanation": "Present simple tense changes to 'is/am/are + past participle' in passive voice.",
                    "marks": 1
                }
            ]
        }
    ]

    exam = manager.create_exam(
        exam_name="CTET 2024 - Paper 1",
        exam_type="CTET",
        description="Central Teacher Eligibility Test for Classes 1-5",
        sections=sections,
        duration_minutes=150,
        total_marks=150,
        passing_marks=90,
        negative_marking=0.0,
        difficulty="medium",
        tags=["2024", "CBSE", "Primary Teacher"]
    )

    print(f"✅ CTET Exam Created: {exam['exam_id']}\n")
    return exam

def create_bpsc_exam():
    """Create BPSC (Bihar Public Service Commission) exam"""
    manager = CompetitiveExamManager()

    print("Creating BPSC 2024 Exam...")

    sections = [
        {
            "section_name": "General Studies",
            "questions": [
                {
                    "question_id": "bpsc_gs_1",
                    "question": "The Indian Constitution was adopted on:",
                    "options": [
                        "15th August 1947",
                        "26th January 1950",
                        "26th November 1949",
                        "15th August 1950"
                    ],
                    "correct_answer": 2,
                    "explanation": "The Constitution was adopted on 26th November 1949 but came into effect on 26th January 1950.",
                    "marks": 2
                },
                {
                    "question_id": "bpsc_gs_2",
                    "question": "Who is known as the 'Father of Indian Constitution'?",
                    "options": [
                        "Mahatma Gandhi",
                        "Jawaharlal Nehru",
                        "Dr. B.R. Ambedkar",
                        "Sardar Vallabhbhai Patel"
                    ],
                    "correct_answer": 2,
                    "explanation": "Dr. B.R. Ambedkar was the chairman of the drafting committee.",
                    "marks": 2
                },
                {
                    "question_id": "bpsc_gs_3",
                    "question": "The first President of India was:",
                    "options": [
                        "Dr. Rajendra Prasad",
                        "Dr. S. Radhakrishnan",
                        "Dr. Zakir Husain",
                        "V.V. Giri"
                    ],
                    "correct_answer": 0,
                    "explanation": "Dr. Rajendra Prasad was the first President of India (1950-1962).",
                    "marks": 2
                }
            ]
        },
        {
            "section_name": "Current Affairs",
            "questions": [
                {
                    "question_id": "bpsc_ca_1",
                    "question": "Which country hosted the G20 Summit in 2023?",
                    "options": [
                        "USA",
                        "India",
                        "Brazil",
                        "China"
                    ],
                    "correct_answer": 1,
                    "explanation": "India hosted the G20 Summit in September 2023 in New Delhi.",
                    "marks": 2
                }
            ]
        }
    ]

    exam = manager.create_exam(
        exam_name="BPSC Prelims 2024",
        exam_type="BPSC",
        description="Bihar Public Service Commission Preliminary Examination",
        sections=sections,
        duration_minutes=120,
        total_marks=200,
        passing_marks=80,
        negative_marking=0.33,
        difficulty="hard",
        tags=["2024", "Bihar", "Civil Services"]
    )

    print(f"✅ BPSC Exam Created: {exam['exam_id']}\n")
    return exam

def create_ssc_cgl_exam():
    """Create SSC CGL (Staff Selection Commission Combined Graduate Level) exam"""
    manager = CompetitiveExamManager()

    print("Creating SSC CGL 2024 Exam...")

    sections = [
        {
            "section_name": "General Intelligence and Reasoning",
            "questions": [
                {
                    "question_id": "ssc_reasoning_1",
                    "question": "Find the odd one out: 3, 5, 11, 14, 17, 21",
                    "options": [
                        "21",
                        "14",
                        "3",
                        "5"
                    ],
                    "correct_answer": 1,
                    "explanation": "All numbers except 14 are prime numbers.",
                    "marks": 2
                }
            ]
        },
        {
            "section_name": "Quantitative Aptitude",
            "questions": [
                {
                    "question_id": "ssc_quant_1",
                    "question": "If the average of 5 numbers is 27, and one number is excluded, the average becomes 25. The excluded number is:",
                    "options": [
                        "30",
                        "35",
                        "40",
                        "45"
                    ],
                    "correct_answer": 1,
                    "explanation": "Sum of 5 numbers = 27 × 5 = 135. Sum of 4 numbers = 25 × 4 = 100. Excluded number = 135 - 100 = 35",
                    "marks": 2
                }
            ]
        },
        {
            "section_name": "English Comprehension",
            "questions": [
                {
                    "question_id": "ssc_eng_1",
                    "question": "Choose the synonym of 'ABUNDANT':",
                    "options": [
                        "Scarce",
                        "Plentiful",
                        "Limited",
                        "Rare"
                    ],
                    "correct_answer": 1,
                    "explanation": "Abundant means plentiful or available in large quantities.",
                    "marks": 2
                }
            ]
        },
        {
            "section_name": "General Awareness",
            "questions": [
                {
                    "question_id": "ssc_ga_1",
                    "question": "The capital of Australia is:",
                    "options": [
                        "Sydney",
                        "Melbourne",
                        "Canberra",
                        "Perth"
                    ],
                    "correct_answer": 2,
                    "explanation": "Canberra is the capital city of Australia, not Sydney.",
                    "marks": 2
                }
            ]
        }
    ]

    exam = manager.create_exam(
        exam_name="SSC CGL 2024 - Tier 1",
        exam_type="SSC CGL",
        description="Staff Selection Commission Combined Graduate Level Tier 1",
        sections=sections,
        duration_minutes=60,
        total_marks=200,
        passing_marks=120,
        negative_marking=0.5,
        difficulty="medium",
        tags=["2024", "SSC", "Graduate Level"]
    )

    print(f"✅ SSC CGL Exam Created: {exam['exam_id']}\n")
    return exam

def create_banking_exam():
    """Create IBPS PO (Banking) exam"""
    manager = CompetitiveExamManager()

    print("Creating IBPS PO 2024 Exam...")

    sections = [
        {
            "section_name": "Reasoning Ability",
            "questions": [
                {
                    "question_id": "bank_reasoning_1",
                    "question": "In a certain code, COMPUTER is written as RFUVQNPC. How is MEDICINE written in that code?",
                    "options": [
                        "EFJDEJMO",
                        "MFEJDJOF",
                        "NFEJDJOF",
                        "EMDFJOJF"
                    ],
                    "correct_answer": 2,
                    "explanation": "Each letter is moved one position forward in the alphabet.",
                    "marks": 1
                }
            ]
        },
        {
            "section_name": "Quantitative Aptitude",
            "questions": [
                {
                    "question_id": "bank_quant_1",
                    "question": "A sum of money at simple interest amounts to Rs. 815 in 3 years and to Rs. 854 in 4 years. The sum is:",
                    "options": [
                        "Rs. 650",
                        "Rs. 690",
                        "Rs. 698",
                        "Rs. 700"
                    ],
                    "correct_answer": 2,
                    "explanation": "Interest for 1 year = 854 - 815 = 39. So, interest for 3 years = 39 × 3 = 117. Principal = 815 - 117 = 698",
                    "marks": 1
                }
            ]
        },
        {
            "section_name": "English Language",
            "questions": [
                {
                    "question_id": "bank_eng_1",
                    "question": "Choose the correct sentence:",
                    "options": [
                        "The news are good.",
                        "The news is good.",
                        "The news were good.",
                        "The news have been good."
                    ],
                    "correct_answer": 1,
                    "explanation": "'News' is an uncountable noun and takes singular verb.",
                    "marks": 1
                }
            ]
        }
    ]

    exam = manager.create_exam(
        exam_name="IBPS PO 2024 - Prelims",
        exam_type="IBPS PO",
        description="Institute of Banking Personnel Selection - Probationary Officer Prelims",
        sections=sections,
        duration_minutes=60,
        total_marks=100,
        passing_marks=40,
        negative_marking=0.25,
        difficulty="medium",
        tags=["2024", "Banking", "PO"]
    )

    print(f"✅ IBPS PO Exam Created: {exam['exam_id']}\n")
    return exam

def main():
    """Create all sample competitive exams"""
    print("="*70)
    print("Creating Sample Competitive Examinations")
    print("="*70)
    print()

    exams = []

    # Create exams
    exams.append(create_stet_exam())
    exams.append(create_ctet_exam())
    exams.append(create_bpsc_exam())
    exams.append(create_ssc_cgl_exam())
    exams.append(create_banking_exam())

    print("="*70)
    print("✅ All Sample Exams Created Successfully!")
    print("="*70)
    print()
    print("Exams Created:")
    for i, exam in enumerate(exams, 1):
        print(f"{i}. {exam['exam_name']}")
        print(f"   ID: {exam['exam_id']}")
        print(f"   Type: {exam['exam_type']}")
        print(f"   Questions: {exam['total_questions']}")
        print(f"   Duration: {exam['duration_minutes']} minutes")
        print(f"   Total Marks: {exam['total_marks']}")
        print()

    print("="*70)
    print("You can now:")
    print("1. Run: streamlit run app.py")
    print("2. Navigate to: Competitive Exams page")
    print("3. View and take these exams")
    print("="*70)

if __name__ == "__main__":
    main()
