"""
Competitive Examination Manager
Support for STET, CTET, BPSC, SSC, UPSC, Banking, Railway and all competitive exams
"""
import json
import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
import random


class CompetitiveExamManager:
    """Manages competitive examinations with MCQ support"""

    def __init__(self, exams_dir: str = "competitive_exams"):
        self.exams_dir = Path(exams_dir)
        self.exams_dir.mkdir(exist_ok=True)

        self.question_bank_dir = self.exams_dir / "question_bank"
        self.question_bank_dir.mkdir(exist_ok=True)

        self.attempts_dir = self.exams_dir / "attempts"
        self.attempts_dir.mkdir(exist_ok=True)

        self.results_dir = self.exams_dir / "results"
        self.results_dir.mkdir(exist_ok=True)

        # Exam categories
        self.exam_categories = {
            "teaching": ["STET", "CTET", "TET", "NET", "SET"],
            "civil_services": ["BPSC", "UPSC", "IAS", "IPS", "State PSC"],
            "banking": ["IBPS PO", "IBPS Clerk", "SBI PO", "SBI Clerk", "RBI Grade B"],
            "ssc": ["SSC CGL", "SSC CHSL", "SSC MTS", "SSC CPO", "SSC GD"],
            "railway": ["RRB NTPC", "RRB Group D", "RRB JE", "RRB ALP"],
            "defense": ["NDA", "CDS", "AFCAT", "Indian Army", "Indian Navy"],
            "engineering": ["GATE", "IES", "PSU Exams"],
            "other": ["Police", "Bank Manager", "LIC", "Insurance", "Custom"]
        }

        # Subject mappings
        self.subject_categories = {
            "teaching": ["Child Development", "Pedagogy", "Mathematics", "Science", "Social Studies", "Hindi", "English"],
            "general": ["General Knowledge", "Current Affairs", "History", "Geography", "Polity", "Economics"],
            "reasoning": ["Logical Reasoning", "Analytical Reasoning", "Verbal Reasoning", "Non-Verbal Reasoning"],
            "quantitative": ["Mathematics", "Arithmetic", "Algebra", "Geometry", "Data Interpretation"],
            "language": ["English", "Hindi", "Grammar", "Comprehension", "Vocabulary"],
            "computer": ["Computer Awareness", "IT Fundamentals", "MS Office", "Internet"],
            "professional": ["Banking Awareness", "Financial Awareness", "Marketing", "Management"]
        }

    def create_exam(
        self,
        exam_name: str,
        exam_type: str,
        description: str,
        sections: List[Dict[str, Any]],
        duration_minutes: int,
        total_marks: int,
        passing_marks: int,
        negative_marking: float = 0.0,
        difficulty: str = "medium",
        tags: List[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new competitive exam

        Args:
            exam_name: Name of exam (e.g., "STET 2024")
            exam_type: Type (e.g., "STET", "CTET", "BPSC")
            description: Exam description
            sections: List of sections with questions
            duration_minutes: Time limit in minutes
            total_marks: Total marks
            passing_marks: Minimum marks to pass
            negative_marking: Negative marks per wrong answer
            difficulty: easy/medium/hard
            tags: Additional tags

        Returns:
            Exam details with exam_id
        """
        exam_id = f"exam_{exam_type.lower().replace(' ', '_')}_{int(time.time())}"

        exam_data = {
            "exam_id": exam_id,
            "exam_name": exam_name,
            "exam_type": exam_type,
            "description": description,
            "sections": sections,
            "duration_minutes": duration_minutes,
            "total_marks": total_marks,
            "passing_marks": passing_marks,
            "negative_marking": negative_marking,
            "difficulty": difficulty,
            "tags": tags or [],
            "created_at": datetime.now().isoformat(),
            "total_questions": sum(len(section["questions"]) for section in sections)
        }

        exam_file = self.exams_dir / f"{exam_id}.json"
        with open(exam_file, 'w', encoding='utf-8') as f:
            json.dump(exam_data, f, indent=2, ensure_ascii=False)

        return exam_data

    def add_question_to_bank(
        self,
        subject: str,
        exam_type: str,
        question: str,
        options: List[str],
        correct_answer: int,
        explanation: str = "",
        marks: int = 1,
        difficulty: str = "medium",
        tags: List[str] = None
    ) -> Dict[str, Any]:
        """
        Add question to question bank

        Args:
            subject: Subject name
            exam_type: Exam type
            question: Question text
            options: List of 4 options
            correct_answer: Index of correct answer (0-3)
            explanation: Explanation of answer
            marks: Marks for this question
            difficulty: easy/medium/hard
            tags: Additional tags

        Returns:
            Question details with question_id
        """
        question_id = f"q_{subject.lower().replace(' ', '_')}_{int(time.time())}_{random.randint(1000, 9999)}"

        question_data = {
            "question_id": question_id,
            "subject": subject,
            "exam_type": exam_type,
            "question": question,
            "options": options,
            "correct_answer": correct_answer,
            "explanation": explanation,
            "marks": marks,
            "difficulty": difficulty,
            "tags": tags or [],
            "added_at": datetime.now().isoformat()
        }

        # Save to subject-specific file
        bank_file = self.question_bank_dir / f"{subject.lower().replace(' ', '_')}.json"

        if bank_file.exists():
            with open(bank_file, 'r', encoding='utf-8') as f:
                questions = json.load(f)
        else:
            questions = []

        questions.append(question_data)

        with open(bank_file, 'w', encoding='utf-8') as f:
            json.dump(questions, f, indent=2, ensure_ascii=False)

        return question_data

    def get_questions_from_bank(
        self,
        subject: str,
        count: int,
        difficulty: Optional[str] = None,
        exam_type: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get questions from question bank"""
        bank_file = self.question_bank_dir / f"{subject.lower().replace(' ', '_')}.json"

        if not bank_file.exists():
            return []

        with open(bank_file, 'r', encoding='utf-8') as f:
            all_questions = json.load(f)

        # Filter by criteria
        filtered = all_questions
        if difficulty:
            filtered = [q for q in filtered if q["difficulty"] == difficulty]
        if exam_type:
            filtered = [q for q in filtered if q["exam_type"] == exam_type]

        # Randomly select questions
        if len(filtered) > count:
            return random.sample(filtered, count)
        return filtered

    def start_exam_attempt(
        self,
        exam_id: str,
        candidate_name: str,
        candidate_email: str,
        candidate_id: str = ""
    ) -> Dict[str, Any]:
        """
        Start an exam attempt

        Args:
            exam_id: Exam ID
            candidate_name: Candidate name
            candidate_email: Candidate email
            candidate_id: Optional candidate/roll number

        Returns:
            Attempt details with attempt_id
        """
        exam_data = self.get_exam(exam_id)
        if not exam_data:
            return {"success": False, "error": "Exam not found"}

        attempt_id = f"attempt_{exam_id}_{int(time.time())}"

        # Calculate end time
        start_time = datetime.now()
        end_time = start_time + timedelta(minutes=exam_data["duration_minutes"])

        attempt_data = {
            "attempt_id": attempt_id,
            "exam_id": exam_id,
            "exam_name": exam_data["exam_name"],
            "candidate_name": candidate_name,
            "candidate_email": candidate_email,
            "candidate_id": candidate_id,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "duration_minutes": exam_data["duration_minutes"],
            "status": "in_progress",
            "answers": {},
            "marked_for_review": [],
            "visited_questions": []
        }

        attempt_file = self.attempts_dir / f"{attempt_id}.json"
        with open(attempt_file, 'w', encoding='utf-8') as f:
            json.dump(attempt_data, f, indent=2, ensure_ascii=False)

        return attempt_data

    def save_answer(
        self,
        attempt_id: str,
        question_id: str,
        selected_option: int,
        mark_for_review: bool = False
    ) -> Dict[str, Any]:
        """Save answer for a question"""
        attempt_file = self.attempts_dir / f"{attempt_id}.json"

        if not attempt_file.exists():
            return {"success": False, "error": "Attempt not found"}

        with open(attempt_file, 'r', encoding='utf-8') as f:
            attempt_data = json.load(f)

        # Save answer
        attempt_data["answers"][question_id] = selected_option

        # Handle mark for review
        if mark_for_review and question_id not in attempt_data["marked_for_review"]:
            attempt_data["marked_for_review"].append(question_id)
        elif not mark_for_review and question_id in attempt_data["marked_for_review"]:
            attempt_data["marked_for_review"].remove(question_id)

        # Track visited questions
        if question_id not in attempt_data["visited_questions"]:
            attempt_data["visited_questions"].append(question_id)

        with open(attempt_file, 'w', encoding='utf-8') as f:
            json.dump(attempt_data, f, indent=2, ensure_ascii=False)

        return {"success": True, "attempt_id": attempt_id}

    def submit_exam(self, attempt_id: str) -> Dict[str, Any]:
        """
        Submit exam and calculate results

        Args:
            attempt_id: Attempt ID

        Returns:
            Result details
        """
        attempt_file = self.attempts_dir / f"{attempt_id}.json"

        if not attempt_file.exists():
            return {"success": False, "error": "Attempt not found"}

        with open(attempt_file, 'r', encoding='utf-8') as f:
            attempt_data = json.load(f)

        # Get exam data
        exam_data = self.get_exam(attempt_data["exam_id"])
        if not exam_data:
            return {"success": False, "error": "Exam not found"}

        # Update attempt status
        attempt_data["status"] = "submitted"
        attempt_data["submitted_at"] = datetime.now().isoformat()

        with open(attempt_file, 'w', encoding='utf-8') as f:
            json.dump(attempt_data, f, indent=2, ensure_ascii=False)

        # Evaluate
        result = self._evaluate_attempt(attempt_data, exam_data)

        # Save result
        result_file = self.results_dir / f"{attempt_id}_result.json"
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        return result

    def _evaluate_attempt(
        self,
        attempt_data: Dict[str, Any],
        exam_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Evaluate exam attempt"""
        correct_answers = 0
        wrong_answers = 0
        unattempted = 0
        total_marks = 0
        negative_marks = 0

        section_results = []

        # Evaluate each section
        for section in exam_data["sections"]:
            section_correct = 0
            section_wrong = 0
            section_unattempted = 0
            section_marks = 0
            section_negative = 0

            question_results = []

            for question in section["questions"]:
                q_id = question["question_id"]
                correct_ans = question["correct_answer"]

                if q_id not in attempt_data["answers"]:
                    # Unattempted
                    unattempted += 1
                    section_unattempted += 1
                    question_results.append({
                        "question_id": q_id,
                        "status": "unattempted",
                        "selected": None,
                        "correct": correct_ans,
                        "is_correct": False,
                        "marks_obtained": 0
                    })
                else:
                    selected_ans = attempt_data["answers"][q_id]

                    if selected_ans == correct_ans:
                        # Correct
                        correct_answers += 1
                        section_correct += 1
                        marks_earned = question.get("marks", 1)
                        total_marks += marks_earned
                        section_marks += marks_earned

                        question_results.append({
                            "question_id": q_id,
                            "status": "correct",
                            "selected": selected_ans,
                            "correct": correct_ans,
                            "is_correct": True,
                            "marks_obtained": marks_earned
                        })
                    else:
                        # Wrong
                        wrong_answers += 1
                        section_wrong += 1
                        neg_marks = exam_data.get("negative_marking", 0)
                        negative_marks += neg_marks
                        section_negative += neg_marks

                        question_results.append({
                            "question_id": q_id,
                            "status": "wrong",
                            "selected": selected_ans,
                            "correct": correct_ans,
                            "is_correct": False,
                            "marks_obtained": -neg_marks
                        })

            section_results.append({
                "section_name": section["section_name"],
                "total_questions": len(section["questions"]),
                "correct": section_correct,
                "wrong": section_wrong,
                "unattempted": section_unattempted,
                "marks_obtained": section_marks - section_negative,
                "negative_marks": section_negative,
                "question_results": question_results
            })

        # Calculate final score
        final_score = total_marks - negative_marks
        total_questions = exam_data["total_questions"]
        passing_marks = exam_data["passing_marks"]
        passed = final_score >= passing_marks

        # Calculate percentile (simplified - in real scenario, compare with all attempts)
        percentage = (final_score / exam_data["total_marks"] * 100) if exam_data["total_marks"] > 0 else 0

        # Calculate accuracy
        attempted = correct_answers + wrong_answers
        accuracy = (correct_answers / attempted * 100) if attempted > 0 else 0

        result = {
            "attempt_id": attempt_data["attempt_id"],
            "exam_id": attempt_data["exam_id"],
            "exam_name": attempt_data["exam_name"],
            "candidate_name": attempt_data["candidate_name"],
            "candidate_email": attempt_data["candidate_email"],
            "candidate_id": attempt_data.get("candidate_id", ""),

            # Summary
            "total_questions": total_questions,
            "attempted": attempted,
            "correct": correct_answers,
            "wrong": wrong_answers,
            "unattempted": unattempted,

            # Marks
            "total_marks_obtained": round(final_score, 2),
            "positive_marks": round(total_marks, 2),
            "negative_marks": round(negative_marks, 2),
            "total_marks": exam_data["total_marks"],
            "passing_marks": passing_marks,

            # Performance
            "percentage": round(percentage, 2),
            "accuracy": round(accuracy, 2),
            "passed": passed,
            "grade": self._calculate_grade(percentage),

            # Section-wise
            "section_results": section_results,

            # Timing
            "start_time": attempt_data["start_time"],
            "end_time": attempt_data.get("submitted_at", attempt_data["end_time"]),
            "evaluated_at": datetime.now().isoformat()
        }

        return result

    def _calculate_grade(self, percentage: float) -> str:
        """Calculate grade based on percentage"""
        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B+"
        elif percentage >= 60:
            return "B"
        elif percentage >= 50:
            return "C"
        elif percentage >= 40:
            return "D"
        else:
            return "F"

    def get_exam(self, exam_id: str) -> Optional[Dict[str, Any]]:
        """Get exam by ID"""
        exam_file = self.exams_dir / f"{exam_id}.json"

        if not exam_file.exists():
            return None

        with open(exam_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_attempt(self, attempt_id: str) -> Optional[Dict[str, Any]]:
        """Get attempt by ID"""
        attempt_file = self.attempts_dir / f"{attempt_id}.json"

        if not attempt_file.exists():
            return None

        with open(attempt_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_result(self, attempt_id: str) -> Optional[Dict[str, Any]]:
        """Get result by attempt ID"""
        result_file = self.results_dir / f"{attempt_id}_result.json"

        if not result_file.exists():
            return None

        with open(result_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_exams(
        self,
        exam_type: Optional[str] = None,
        difficulty: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List all exams with optional filtering"""
        exams = []

        for exam_file in self.exams_dir.glob("exam_*.json"):
            with open(exam_file, 'r', encoding='utf-8') as f:
                exam_data = json.load(f)

                # Apply filters
                if exam_type and exam_data["exam_type"] != exam_type:
                    continue
                if difficulty and exam_data["difficulty"] != difficulty:
                    continue

                exams.append({
                    "exam_id": exam_data["exam_id"],
                    "exam_name": exam_data["exam_name"],
                    "exam_type": exam_data["exam_type"],
                    "difficulty": exam_data["difficulty"],
                    "total_questions": exam_data["total_questions"],
                    "total_marks": exam_data["total_marks"],
                    "duration_minutes": exam_data["duration_minutes"],
                    "created_at": exam_data["created_at"]
                })

        return sorted(exams, key=lambda x: x["created_at"], reverse=True)

    def list_attempts(
        self,
        exam_id: Optional[str] = None,
        candidate_email: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """List exam attempts with optional filtering"""
        attempts = []

        for attempt_file in self.attempts_dir.glob("attempt_*.json"):
            with open(attempt_file, 'r', encoding='utf-8') as f:
                attempt_data = json.load(f)

                # Apply filters
                if exam_id and attempt_data["exam_id"] != exam_id:
                    continue
                if candidate_email and attempt_data["candidate_email"] != candidate_email:
                    continue

                attempts.append({
                    "attempt_id": attempt_data["attempt_id"],
                    "exam_name": attempt_data["exam_name"],
                    "candidate_name": attempt_data["candidate_name"],
                    "candidate_email": attempt_data["candidate_email"],
                    "start_time": attempt_data["start_time"],
                    "status": attempt_data["status"]
                })

        return sorted(attempts, key=lambda x: x["start_time"], reverse=True)

    def get_exam_analytics(self, exam_id: str) -> Dict[str, Any]:
        """Get analytics for an exam"""
        # Get all attempts for this exam
        attempts = self.list_attempts(exam_id=exam_id)

        if not attempts:
            return {"success": False, "error": "No attempts found"}

        total_attempts = len(attempts)
        submitted = len([a for a in attempts if a["status"] == "submitted"])

        # Get results
        results = []
        for attempt in attempts:
            if attempt["status"] == "submitted":
                result = self.get_result(attempt["attempt_id"])
                if result:
                    results.append(result)

        if not results:
            return {
                "exam_id": exam_id,
                "total_attempts": total_attempts,
                "submitted": submitted,
                "message": "No submitted attempts yet"
            }

        # Calculate statistics
        scores = [r["total_marks_obtained"] for r in results]
        percentages = [r["percentage"] for r in results]
        passed_count = len([r for r in results if r["passed"]])

        analytics = {
            "exam_id": exam_id,
            "total_attempts": total_attempts,
            "submitted": submitted,
            "passed": passed_count,
            "failed": submitted - passed_count,
            "pass_percentage": round(passed_count / submitted * 100, 2) if submitted > 0 else 0,

            "scores": {
                "average": round(sum(scores) / len(scores), 2),
                "highest": round(max(scores), 2),
                "lowest": round(min(scores), 2)
            },

            "percentages": {
                "average": round(sum(percentages) / len(percentages), 2),
                "highest": round(max(percentages), 2),
                "lowest": round(min(percentages), 2)
            },

            "top_scorers": sorted(
                [{"name": r["candidate_name"], "score": r["total_marks_obtained"],
                  "percentage": r["percentage"]} for r in results],
                key=lambda x: x["score"],
                reverse=True
            )[:10]
        }

        return analytics
