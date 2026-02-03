"""
Batch Processing Script - Process multiple topics in parallel using AI agents
Demonstrates multiprocessing capabilities of the AI Multi-Agent system
"""
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parallel_crew_manager import ParallelCrewManager, benchmark_parallel_vs_sequential
from src.presentation_exporter import export_presentation_parallel
import json
from datetime import datetime


def batch_generate_articles():
    """Generate multiple articles in parallel"""
    print("="*80)
    print("📝 BATCH ARTICLE GENERATION")
    print("="*80)
    print()

    topics = [
        "Artificial Intelligence in Healthcare 2026",
        "Machine Learning Best Practices",
        "Python Programming Tips for Beginners",
        "Cloud Computing Trends",
        "Cybersecurity Fundamentals"
    ]

    print(f"Topics to process: {len(topics)}")
    for i, topic in enumerate(topics, 1):
        print(f"  {i}. {topic}")
    print()

    manager = ParallelCrewManager(max_workers=3)
    results = manager.execute_batch_research(topics, content_type="blog post")

    # Save results
    output_dir = Path("output/batch_articles")
    output_dir.mkdir(parents=True, exist_ok=True)

    for topic, result in results.items():
        if result['success']:
            filename = topic.replace(" ", "_").replace("/", "_")[:50] + ".md"
            filepath = output_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(result['result']))
            print(f"✅ Saved: {filepath}")

    print(f"\n📁 All articles saved to: {output_dir}")
    return results


def batch_generate_presentations():
    """Generate multiple presentations in parallel"""
    print("="*80)
    print("🎨 BATCH PRESENTATION GENERATION")
    print("="*80)
    print()

    topics = [
        "Introduction to Machine Learning",
        "Python Programming Fundamentals",
        "Web Development with React"
    ]

    print(f"Presentations to generate: {len(topics)}")
    for i, topic in enumerate(topics, 1):
        print(f"  {i}. {topic}")
    print()

    manager = ParallelCrewManager(max_workers=2)
    results = manager.execute_batch_presentations(topics)

    # Save and export each presentation
    output_dir = Path("output/batch_presentations")
    output_dir.mkdir(parents=True, exist_ok=True)

    for topic, result in results.items():
        if result['success']:
            content = str(result['result'])
            filename = topic.replace(" ", "_")[:50]

            # Save markdown
            md_file = output_dir / f"{filename}.md"
            with open(md_file, 'w', encoding='utf-8') as f:
                f.write(content)

            # Export to all formats in parallel
            print(f"\n⚡ Exporting '{topic}' to all formats...")
            exports = export_presentation_parallel(content, topic)

            # Save PowerPoint
            if 'pptx' in exports and not isinstance(exports['pptx'], str):
                pptx_file = output_dir / f"{filename}.pptx"
                with open(pptx_file, 'wb') as f:
                    f.write(exports['pptx'].read())
                print(f"  ✅ {pptx_file.name}")

            # Save HTML
            if 'html' in exports:
                html_file = output_dir / f"{filename}.html"
                with open(html_file, 'w', encoding='utf-8') as f:
                    f.write(exports['html'])
                print(f"  ✅ {html_file.name}")

            # Save PDF
            if 'pdf' in exports and not isinstance(exports['pdf'], str):
                pdf_file = output_dir / f"{filename}.pdf"
                with open(pdf_file, 'wb') as f:
                    f.write(exports['pdf'].read())
                print(f"  ✅ {pdf_file.name}")

    print(f"\n📁 All presentations saved to: {output_dir}")
    return results


def mixed_batch_processing():
    """Process mixed content types in parallel"""
    print("="*80)
    print("🔄 MIXED BATCH PROCESSING")
    print("="*80)
    print()

    tasks = [
        {'topic': 'AI in Healthcare', 'content_type': 'article'},
        {'topic': 'Python Tips', 'content_type': 'blog post'},
        {'topic': 'Machine Learning Basics', 'content_type': 'presentation'},
        {'topic': 'Web Development Guide', 'content_type': 'report'}
    ]

    print("Tasks to process:")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task['topic']} ({task['content_type']})")
    print()

    manager = ParallelCrewManager(max_workers=4)
    results = manager.execute_parallel_workflows(tasks)

    # Save results
    output_dir = Path("output/mixed_batch")
    output_dir.mkdir(parents=True, exist_ok=True)

    for result in results:
        if result['success']:
            topic = result['topic']
            content_type = result['content_type']
            filename = f"{topic.replace(' ', '_')}_{content_type}.md"
            filepath = output_dir / filename
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(result['result']))
            print(f"✅ Saved: {filepath}")

    print(f"\n📁 All content saved to: {output_dir}")
    return results


def run_benchmark():
    """Run benchmark comparing parallel vs sequential"""
    print("="*80)
    print("📊 PARALLEL vs SEQUENTIAL BENCHMARK")
    print("="*80)
    print()

    topics = [
        "AI Trends 2026",
        "Python Best Practices",
        "Cloud Computing Guide"
    ]

    print(f"Benchmark topics: {len(topics)}")
    for i, topic in enumerate(topics, 1):
        print(f"  {i}. {topic}")
    print()

    results = benchmark_parallel_vs_sequential(topics, content_type="blog post")

    print("\n💾 Saving benchmark results...")
    output_file = Path("output/benchmark_results.json")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    results['timestamp'] = datetime.now().isoformat()
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"✅ Results saved to: {output_file}")
    return results


def main():
    """Main menu"""
    print("\n" + "="*80)
    print("⚡ PARALLEL AI AGENT BATCH PROCESSING")
    print("="*80)
    print("\nChoose an option:")
    print("  1. Batch generate articles (5 topics)")
    print("  2. Batch generate presentations (3 topics)")
    print("  3. Mixed batch processing (4 different content types)")
    print("  4. Run performance benchmark")
    print("  5. Exit")
    print()

    choice = input("Enter choice (1-5): ").strip()

    if choice == '1':
        batch_generate_articles()
    elif choice == '2':
        batch_generate_presentations()
    elif choice == '3':
        mixed_batch_processing()
    elif choice == '4':
        run_benchmark()
    elif choice == '5':
        print("\n👋 Goodbye!")
        return
    else:
        print("\n❌ Invalid choice")

    print("\n✅ Done!")


if __name__ == "__main__":
    main()
