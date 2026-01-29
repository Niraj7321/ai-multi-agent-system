"""
Coding Test & Examination Manager
Create, manage, and evaluate coding tests
"""
import json
import os
import sys
import subprocess
import tempfile
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional
import traceback


class CodingTestManager:
    """Manages coding tests and examinations"""

    def __init__(self, tests_dir: str = "tests_data"):
        self.tests_dir = Path(tests_dir)
        self.tests_dir.mkdir(exist_ok=True)

        self.submissions_dir = self.tests_dir / "submissions"
        self.submissions_dir.mkdir(exist_ok=True)

        self.results_dir = self.tests_dir / "results"
        self.results_dir.mkdir(exist_ok=True)

    def create_test(
        self,
        title: str,
        description: str,
        questions: List[Dict[str, Any]],
        time_limit_minutes: int = 60,
        difficulty: str = "medium",
        tags: List[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new coding test

        Args:
            title: Test title
            description: Test description
            questions: List of questions with test cases
            time_limit_minutes: Time limit in minutes
            difficulty: easy/medium/hard
            tags: List of tags (e.g., ["Python", "Algorithms"])

        Returns:
            Test details with test_id
        """
        test_id = f"test_{int(time.time())}"

        test_data = {
            "test_id": test_id,
            "title": title,
            "description": description,
            "questions": questions,
            "time_limit_minutes": time_limit_minutes,
            "difficulty": difficulty,
            "tags": tags or [],
            "created_at": datetime.now().isoformat(),
            "total_points": sum(q.get("points", 10) for q in questions)
        }

        test_file = self.tests_dir / f"{test_id}.json"
        with open(test_file, 'w', encoding='utf-8') as f:
            json.dump(test_data, f, indent=2, ensure_ascii=False)

        return test_data

    def get_test(self, test_id: str) -> Optional[Dict[str, Any]]:
        """Get test by ID"""
        test_file = self.tests_dir / f"{test_id}.json"

        if not test_file.exists():
            return None

        with open(test_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_tests(self) -> List[Dict[str, Any]]:
        """List all available tests"""
        tests = []

        for test_file in self.tests_dir.glob("test_*.json"):
            with open(test_file, 'r', encoding='utf-8') as f:
                test_data = json.load(f)
                tests.append({
                    "test_id": test_data["test_id"],
                    "title": test_data["title"],
                    "difficulty": test_data["difficulty"],
                    "questions": len(test_data["questions"]),
                    "time_limit": test_data["time_limit_minutes"],
                    "total_points": test_data["total_points"],
                    "created_at": test_data["created_at"]
                })

        return sorted(tests, key=lambda x: x["created_at"], reverse=True)

    def submit_answer(
        self,
        test_id: str,
        candidate_name: str,
        candidate_email: str,
        answers: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Submit test answers

        Args:
            test_id: Test ID
            candidate_name: Candidate's name
            candidate_email: Candidate's email
            answers: List of answers with code

        Returns:
            Submission details with submission_id
        """
        submission_id = f"sub_{test_id}_{int(time.time())}"

        submission_data = {
            "submission_id": submission_id,
            "test_id": test_id,
            "candidate_name": candidate_name,
            "candidate_email": candidate_email,
            "answers": answers,
            "submitted_at": datetime.now().isoformat(),
            "status": "pending"
        }

        submission_file = self.submissions_dir / f"{submission_id}.json"
        with open(submission_file, 'w', encoding='utf-8') as f:
            json.dump(submission_data, f, indent=2, ensure_ascii=False)

        return submission_data

    def run_code(
        self,
        code: str,
        language: str,
        test_input: str = "",
        timeout: int = 5
    ) -> Dict[str, Any]:
        """
        Execute code and return output

        Args:
            code: Source code to execute
            language: Programming language (python, javascript, java, cpp)
            test_input: Input to provide to the program
            timeout: Execution timeout in seconds

        Returns:
            Execution result with output, errors, execution_time
        """
        start_time = time.time()

        try:
            if language.lower() == "python":
                return self._run_python_code(code, test_input, timeout)
            elif language.lower() in ["javascript", "js", "node"]:
                return self._run_javascript_code(code, test_input, timeout)
            elif language.lower() == "java":
                return self._run_java_code(code, test_input, timeout)
            elif language.lower() in ["cpp", "c++"]:
                return self._run_cpp_code(code, test_input, timeout)
            else:
                return {
                    "success": False,
                    "error": f"Unsupported language: {language}",
                    "output": "",
                    "execution_time": 0
                }

        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "output": "",
                "execution_time": time.time() - start_time
            }

    def _run_python_code(self, code: str, test_input: str, timeout: int) -> Dict[str, Any]:
        """Run Python code"""
        start_time = time.time()

        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, encoding='utf-8') as f:
            f.write(code)
            temp_file = f.name

        try:
            result = subprocess.run(
                [sys.executable, temp_file],
                input=test_input,
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
            )

            execution_time = time.time() - start_time

            return {
                "success": result.returncode == 0,
                "output": result.stdout.strip(),
                "error": result.stderr.strip() if result.stderr else "",
                "execution_time": execution_time,
                "return_code": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": f"Execution timeout ({timeout}s exceeded)",
                "execution_time": timeout,
                "return_code": -1
            }

        finally:
            try:
                os.unlink(temp_file)
            except:
                pass

    def _run_javascript_code(self, code: str, test_input: str, timeout: int) -> Dict[str, Any]:
        """Run JavaScript code using Node.js"""
        start_time = time.time()

        # Check if Node.js is available
        try:
            subprocess.run(["node", "--version"], capture_output=True, timeout=2)
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return {
                "success": False,
                "error": "Node.js is not installed. Please install Node.js to run JavaScript code.",
                "output": "",
                "execution_time": 0
            }

        with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False, encoding='utf-8') as f:
            f.write(code)
            temp_file = f.name

        try:
            result = subprocess.run(
                ["node", temp_file],
                input=test_input,
                capture_output=True,
                text=True,
                timeout=timeout,
                encoding='utf-8',
                errors='replace'
            )

            execution_time = time.time() - start_time

            return {
                "success": result.returncode == 0,
                "output": result.stdout.strip(),
                "error": result.stderr.strip() if result.stderr else "",
                "execution_time": execution_time,
                "return_code": result.returncode
            }

        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": f"Execution timeout ({timeout}s exceeded)",
                "execution_time": timeout,
                "return_code": -1
            }

        finally:
            try:
                os.unlink(temp_file)
            except:
                pass

    def _run_java_code(self, code: str, test_input: str, timeout: int) -> Dict[str, Any]:
        """Run Java code"""
        # Extract class name from code
        import re
        class_match = re.search(r'public\s+class\s+(\w+)', code)
        if not class_match:
            return {
                "success": False,
                "error": "Could not find public class declaration",
                "output": "",
                "execution_time": 0
            }

        class_name = class_match.group(1)

        # Check if Java is available
        try:
            subprocess.run(["javac", "-version"], capture_output=True, timeout=2)
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return {
                "success": False,
                "error": "Java compiler (javac) is not installed.",
                "output": "",
                "execution_time": 0
            }

        start_time = time.time()

        with tempfile.TemporaryDirectory() as temp_dir:
            java_file = Path(temp_dir) / f"{class_name}.java"
            with open(java_file, 'w', encoding='utf-8') as f:
                f.write(code)

            try:
                # Compile
                compile_result = subprocess.run(
                    ["javac", str(java_file)],
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=temp_dir
                )

                if compile_result.returncode != 0:
                    return {
                        "success": False,
                        "output": "",
                        "error": f"Compilation error:\n{compile_result.stderr}",
                        "execution_time": time.time() - start_time,
                        "return_code": compile_result.returncode
                    }

                # Run
                run_result = subprocess.run(
                    ["java", class_name],
                    input=test_input,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    cwd=temp_dir,
                    encoding='utf-8',
                    errors='replace'
                )

                execution_time = time.time() - start_time

                return {
                    "success": run_result.returncode == 0,
                    "output": run_result.stdout.strip(),
                    "error": run_result.stderr.strip() if run_result.stderr else "",
                    "execution_time": execution_time,
                    "return_code": run_result.returncode
                }

            except subprocess.TimeoutExpired:
                return {
                    "success": False,
                    "output": "",
                    "error": f"Execution timeout ({timeout}s exceeded)",
                    "execution_time": timeout,
                    "return_code": -1
                }

    def _run_cpp_code(self, code: str, test_input: str, timeout: int) -> Dict[str, Any]:
        """Run C++ code"""
        # Check if g++ is available
        try:
            subprocess.run(["g++", "--version"], capture_output=True, timeout=2)
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return {
                "success": False,
                "error": "g++ compiler is not installed.",
                "output": "",
                "execution_time": 0
            }

        start_time = time.time()

        with tempfile.TemporaryDirectory() as temp_dir:
            cpp_file = Path(temp_dir) / "main.cpp"
            exe_file = Path(temp_dir) / "main.exe"

            with open(cpp_file, 'w', encoding='utf-8') as f:
                f.write(code)

            try:
                # Compile
                compile_result = subprocess.run(
                    ["g++", str(cpp_file), "-o", str(exe_file)],
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )

                if compile_result.returncode != 0:
                    return {
                        "success": False,
                        "output": "",
                        "error": f"Compilation error:\n{compile_result.stderr}",
                        "execution_time": time.time() - start_time,
                        "return_code": compile_result.returncode
                    }

                # Run
                run_result = subprocess.run(
                    [str(exe_file)],
                    input=test_input,
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    encoding='utf-8',
                    errors='replace'
                )

                execution_time = time.time() - start_time

                return {
                    "success": run_result.returncode == 0,
                    "output": run_result.stdout.strip(),
                    "error": run_result.stderr.strip() if run_result.stderr else "",
                    "execution_time": execution_time,
                    "return_code": run_result.returncode
                }

            except subprocess.TimeoutExpired:
                return {
                    "success": False,
                    "output": "",
                    "error": f"Execution timeout ({timeout}s exceeded)",
                    "execution_time": timeout,
                    "return_code": -1
                }

    def evaluate_submission(self, submission_id: str) -> Dict[str, Any]:
        """
        Evaluate a submission against test cases

        Args:
            submission_id: Submission ID

        Returns:
            Evaluation results with score and feedback
        """
        # Load submission
        submission_file = self.submissions_dir / f"{submission_id}.json"
        if not submission_file.exists():
            return {"success": False, "error": "Submission not found"}

        with open(submission_file, 'r', encoding='utf-8') as f:
            submission = json.load(f)

        # Load test
        test_data = self.get_test(submission["test_id"])
        if not test_data:
            return {"success": False, "error": "Test not found"}

        # Evaluate each answer
        results = []
        total_score = 0
        max_score = 0

        for i, (question, answer) in enumerate(zip(test_data["questions"], submission["answers"])):
            question_result = self._evaluate_answer(question, answer)
            results.append(question_result)

            total_score += question_result["score"]
            max_score += question.get("points", 10)

        # Calculate percentage
        percentage = (total_score / max_score * 100) if max_score > 0 else 0

        # Determine pass/fail
        passing_score = test_data.get("passing_percentage", 60)
        passed = percentage >= passing_score

        evaluation = {
            "submission_id": submission_id,
            "test_id": submission["test_id"],
            "candidate_name": submission["candidate_name"],
            "candidate_email": submission["candidate_email"],
            "total_score": total_score,
            "max_score": max_score,
            "percentage": round(percentage, 2),
            "passed": passed,
            "results": results,
            "evaluated_at": datetime.now().isoformat()
        }

        # Save results
        result_file = self.results_dir / f"{submission_id}_result.json"
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(evaluation, f, indent=2, ensure_ascii=False)

        return evaluation

    def _evaluate_answer(self, question: Dict[str, Any], answer: Dict[str, Any]) -> Dict[str, Any]:
        """Evaluate a single answer against test cases"""
        code = answer.get("code", "")
        language = question.get("language", "python")
        test_cases = question.get("test_cases", [])
        points = question.get("points", 10)

        if not code.strip():
            return {
                "question_id": question.get("id", ""),
                "question_title": question.get("title", ""),
                "score": 0,
                "max_score": points,
                "passed_tests": 0,
                "total_tests": len(test_cases),
                "test_results": [],
                "feedback": "No code submitted"
            }

        test_results = []
        passed_count = 0

        for i, test_case in enumerate(test_cases):
            test_input = test_case.get("input", "")
            expected_output = test_case.get("expected_output", "").strip()

            # Run code
            run_result = self.run_code(code, language, test_input, timeout=5)

            # Check output
            actual_output = run_result.get("output", "").strip()
            passed = run_result["success"] and actual_output == expected_output

            if passed:
                passed_count += 1

            test_results.append({
                "test_case": i + 1,
                "passed": passed,
                "input": test_input,
                "expected": expected_output,
                "actual": actual_output,
                "error": run_result.get("error", ""),
                "execution_time": run_result.get("execution_time", 0)
            })

        # Calculate score
        score = (passed_count / len(test_cases) * points) if test_cases else 0

        return {
            "question_id": question.get("id", ""),
            "question_title": question.get("title", ""),
            "score": round(score, 2),
            "max_score": points,
            "passed_tests": passed_count,
            "total_tests": len(test_cases),
            "test_results": test_results,
            "feedback": f"Passed {passed_count}/{len(test_cases)} test cases"
        }

    def get_result(self, submission_id: str) -> Optional[Dict[str, Any]]:
        """Get evaluation result"""
        result_file = self.results_dir / f"{submission_id}_result.json"

        if not result_file.exists():
            return None

        with open(result_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def list_submissions(self, test_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """List all submissions, optionally filtered by test_id"""
        submissions = []

        for submission_file in self.submissions_dir.glob("sub_*.json"):
            with open(submission_file, 'r', encoding='utf-8') as f:
                submission = json.load(f)

                if test_id and submission["test_id"] != test_id:
                    continue

                # Check if evaluated
                result_file = self.results_dir / f"{submission['submission_id']}_result.json"
                evaluated = result_file.exists()

                submissions.append({
                    "submission_id": submission["submission_id"],
                    "test_id": submission["test_id"],
                    "candidate_name": submission["candidate_name"],
                    "candidate_email": submission["candidate_email"],
                    "submitted_at": submission["submitted_at"],
                    "evaluated": evaluated
                })

        return sorted(submissions, key=lambda x: x["submitted_at"], reverse=True)
