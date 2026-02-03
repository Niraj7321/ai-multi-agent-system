"""
Parallel Crew Manager - Multiprocessing support for AI agents
Enables parallel execution of multiple workflows and batch processing
"""
from typing import List, Dict, Any, Optional
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from multiprocessing import cpu_count
import time

from src.crew_manager import CrewManager
from src.logger import logger


class ParallelCrewManager:
    """
    Manages parallel execution of AI agent workflows
    Supports batch processing and concurrent task execution
    """

    def __init__(
        self,
        model_name: str = "claude-sonnet-4-20250514",
        temperature: float = 0.7,
        api_key: Optional[str] = None,
        use_anthropic: bool = None,
        max_workers: Optional[int] = None
    ):
        """
        Initialize Parallel Crew Manager

        Args:
            model_name: LLM model name
            temperature: Temperature setting
            api_key: API key (optional)
            use_anthropic: Use Anthropic Claude (auto-detected if None)
            max_workers: Maximum parallel workers (default: cpu_count)
        """
        self.model_name = model_name
        self.temperature = temperature
        self.api_key = api_key
        self.use_anthropic = use_anthropic
        self.max_workers = max_workers or cpu_count()

        logger.info(f"⚡ Parallel Crew Manager initialized with {self.max_workers} workers")

    def execute_batch_research(
        self,
        topics: List[str],
        content_type: str = "article"
    ) -> Dict[str, Dict[str, Any]]:
        """
        Execute research workflow for multiple topics in parallel

        Args:
            topics: List of research topics
            content_type: Type of content to create

        Returns:
            Dictionary mapping topic to workflow result

        Example:
            >>> manager = ParallelCrewManager()
            >>> topics = ["AI in Healthcare", "Machine Learning Basics", "Python Tips"]
            >>> results = manager.execute_batch_research(topics)
            >>> # All 3 topics processed simultaneously!
        """
        logger.info(f"🚀 Starting batch research for {len(topics)} topics")
        logger.info(f"⚡ Using {self.max_workers} parallel workers")

        results = {}
        start_time = time.time()

        # Use ThreadPoolExecutor for API-bound operations
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all tasks
            future_to_topic = {}
            for topic in topics:
                # Create separate CrewManager for each task
                manager = CrewManager(
                    model_name=self.model_name,
                    temperature=self.temperature,
                    api_key=self.api_key,
                    use_anthropic=self.use_anthropic
                )

                future = executor.submit(
                    manager.execute_research_workflow,
                    topic,
                    content_type
                )
                future_to_topic[future] = topic

            # Collect results as they complete
            completed = 0
            for future in as_completed(future_to_topic):
                topic = future_to_topic[future]
                completed += 1

                try:
                    result = future.result()
                    results[topic] = result
                    status = "✅" if result['success'] else "❌"
                    logger.info(f"{status} [{completed}/{len(topics)}] {topic}")
                except Exception as e:
                    logger.error(f"❌ Error processing {topic}: {str(e)}")
                    results[topic] = {
                        "success": False,
                        "topic": topic,
                        "error": str(e)
                    }

        elapsed = time.time() - start_time
        success_count = sum(1 for r in results.values() if r.get('success'))

        logger.info(f"\n{'='*80}")
        logger.info(f"📊 BATCH PROCESSING COMPLETE")
        logger.info(f"{'='*80}")
        logger.info(f"✅ Successful: {success_count}/{len(topics)}")
        logger.info(f"⏱️  Total time: {elapsed:.1f}s")
        logger.info(f"⚡ Avg time per topic: {elapsed/len(topics):.1f}s")
        logger.info(f"{'='*80}\n")

        return results

    def execute_batch_presentations(
        self,
        topics: List[str]
    ) -> Dict[str, Dict[str, Any]]:
        """
        Generate presentations for multiple topics in parallel

        Args:
            topics: List of presentation topics

        Returns:
            Dictionary mapping topic to presentation result

        Example:
            >>> manager = ParallelCrewManager()
            >>> topics = ["AI Trends 2026", "Python Best Practices"]
            >>> presentations = manager.execute_batch_presentations(topics)
        """
        logger.info(f"🎨 Starting batch presentation generation for {len(topics)} topics")
        logger.info(f"⚡ Using {self.max_workers} parallel workers")

        results = {}
        start_time = time.time()

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_topic = {}
            for topic in topics:
                manager = CrewManager(
                    model_name=self.model_name,
                    temperature=self.temperature,
                    api_key=self.api_key,
                    use_anthropic=self.use_anthropic
                )

                future = executor.submit(
                    manager.execute_presentation_workflow,
                    topic
                )
                future_to_topic[future] = topic

            completed = 0
            for future in as_completed(future_to_topic):
                topic = future_to_topic[future]
                completed += 1

                try:
                    result = future.result()
                    results[topic] = result
                    status = "✅" if result['success'] else "❌"
                    logger.info(f"{status} [{completed}/{len(topics)}] {topic}")
                except Exception as e:
                    logger.error(f"❌ Error processing {topic}: {str(e)}")
                    results[topic] = {
                        "success": False,
                        "topic": topic,
                        "error": str(e)
                    }

        elapsed = time.time() - start_time
        success_count = sum(1 for r in results.values() if r.get('success'))

        logger.info(f"\n{'='*80}")
        logger.info(f"🎨 BATCH PRESENTATION GENERATION COMPLETE")
        logger.info(f"{'='*80}")
        logger.info(f"✅ Successful: {success_count}/{len(topics)}")
        logger.info(f"⏱️  Total time: {elapsed:.1f}s")
        logger.info(f"⚡ Avg time per presentation: {elapsed/len(topics):.1f}s")
        logger.info(f"{'='*80}\n")

        return results

    def execute_parallel_workflows(
        self,
        tasks: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Execute multiple workflows in parallel with different configurations

        Args:
            tasks: List of task configurations
                Each task should have:
                - 'topic': str
                - 'content_type': str ('article', 'blog post', 'presentation', etc.)
                - 'model_name': str (optional, uses default if not specified)

        Returns:
            List of workflow results

        Example:
            >>> tasks = [
            ...     {'topic': 'AI Healthcare', 'content_type': 'article'},
            ...     {'topic': 'ML Basics', 'content_type': 'blog post'},
            ...     {'topic': 'Python Tips', 'content_type': 'presentation'}
            ... ]
            >>> results = manager.execute_parallel_workflows(tasks)
        """
        logger.info(f"🔄 Starting parallel execution of {len(tasks)} workflows")
        logger.info(f"⚡ Using {self.max_workers} parallel workers")

        results = []
        start_time = time.time()

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for task in tasks:
                topic = task['topic']
                content_type = task.get('content_type', 'article')
                model = task.get('model_name', self.model_name)

                manager = CrewManager(
                    model_name=model,
                    temperature=self.temperature,
                    api_key=self.api_key,
                    use_anthropic=self.use_anthropic
                )

                if content_type == 'presentation':
                    future = executor.submit(manager.execute_presentation_workflow, topic)
                else:
                    future = executor.submit(manager.execute_research_workflow, topic, content_type)

                futures.append((future, task))

            completed = 0
            for future, task in futures:
                completed += 1
                try:
                    result = future.result()
                    results.append(result)
                    status = "✅" if result['success'] else "❌"
                    logger.info(f"{status} [{completed}/{len(tasks)}] {task['topic']} ({task.get('content_type', 'article')})")
                except Exception as e:
                    logger.error(f"❌ Error processing {task['topic']}: {str(e)}")
                    results.append({
                        "success": False,
                        "topic": task['topic'],
                        "error": str(e)
                    })

        elapsed = time.time() - start_time
        success_count = sum(1 for r in results if r.get('success'))

        logger.info(f"\n{'='*80}")
        logger.info(f"🔄 PARALLEL WORKFLOWS COMPLETE")
        logger.info(f"{'='*80}")
        logger.info(f"✅ Successful: {success_count}/{len(tasks)}")
        logger.info(f"⏱️  Total time: {elapsed:.1f}s")
        logger.info(f"⚡ Avg time per workflow: {elapsed/len(tasks):.1f}s")
        logger.info(f"{'='*80}\n")

        return results


def benchmark_parallel_vs_sequential(topics: List[str], content_type: str = "article"):
    """
    Benchmark parallel vs sequential processing

    Args:
        topics: List of topics to process
        content_type: Type of content

    Returns:
        Dictionary with benchmark results
    """
    logger.info("📊 Starting benchmark: Parallel vs Sequential")

    # Sequential processing
    logger.info("\n1️⃣ Running sequential processing...")
    sequential_start = time.time()
    manager = CrewManager()
    sequential_results = []
    for topic in topics:
        result = manager.execute_research_workflow(topic, content_type)
        sequential_results.append(result)
    sequential_time = time.time() - sequential_start

    # Parallel processing
    logger.info("\n2️⃣ Running parallel processing...")
    parallel_start = time.time()
    parallel_manager = ParallelCrewManager()
    parallel_results = parallel_manager.execute_batch_research(topics, content_type)
    parallel_time = time.time() - parallel_start

    # Calculate speedup
    speedup = sequential_time / parallel_time

    logger.info(f"\n{'='*80}")
    logger.info(f"📊 BENCHMARK RESULTS")
    logger.info(f"{'='*80}")
    logger.info(f"Topics processed: {len(topics)}")
    logger.info(f"Sequential time: {sequential_time:.1f}s")
    logger.info(f"Parallel time: {parallel_time:.1f}s")
    logger.info(f"⚡ Speedup: {speedup:.2f}x faster!")
    logger.info(f"{'='*80}\n")

    return {
        'topics': len(topics),
        'sequential_time': sequential_time,
        'parallel_time': parallel_time,
        'speedup': speedup
    }
