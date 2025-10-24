import os
from datetime import datetime
from flask import Flask, render_template, send_file, jsonify, request
from supabase import create_client
from dotenv import load_dotenv
from flask import send_file


load_dotenv()

app = Flask(__name__)

supabase = create_client(
    os.getenv('VITE_SUPABASE_URL'),
    os.getenv('VITE_SUPABASE_ANON_KEY')
)

RESUME_DATA = {
    'name': 'Chintan Gaur',
    'title': 'DATA AND GENERATIVE AI ENGINEER',
    'contact': {
        'phone': '+91-7895687477',
        'email': 'gaurchintan@gmail.com',
        'github': 'github.com/EonFlash',
        'linkedin': 'linkedin.com/in/chintangaur'
    },
    'summary': 'GenAI Data Engineer with over 2 years building production RAG systems, fine-tuning LLMs, and integrating FAISS and Pinecone vector databases for scalable semantic search. Skilled in document ingestion, embedding pipelines, and agentic ETL migration POCs. Certified: Oracle AI Vector Search Professional; LTIMindtree IGNITE.',
    'experience': [
        {
            'company': 'LTIMindtree',
            'location': 'Bangalore, India',
            'position': 'Data and GenAI Engineer',
            'period': 'Jun 2024 - Present',
            'achievements': [
                'Architected and spearheaded enterprise-grade RAG pipelines using Hugging Face and LangChain, achieving a 40% reduction in query latency during document data extraction.',
                'Implemented and fine-tuned FAISS and Pinecone vector databases with bespoke, intelligent chunking strategies, reducing retrieval time by 65% and achieving average response speeds under 800 ms during document data extraction.',
                'Fine-tuned and calibrated small LLM using LoRA and Parameter-Efficient Fine Tuning techniques to automate SAS-to-PySpark code translation, achieving 90% functional accuracy and accelerating ETL migration workflows by 60%.',
                'Engineered and deployed AI-driven humanization and PII redaction pipelines, slashing manual content review time by 70% and achieving 95% accuracy in sensitive-data removal.',
                'Designed and integrated prompt-injection protection and reasoning-agent frameworks with human-in-the-loop validation, improving system security posture by 95% and boosting LLM response correctness by 30%.'
            ]
        },
        {
            'company': 'HORIBA Ltd',
            'location': 'Delhi, India',
            'position': 'AI - ML Engineer',
            'period': 'March 2024 - Jun 2024',
            'achievements': [
                'Built foundational proficiency in AI/ML and Python: data preprocessing, feature engineering, model evaluation.',
                'Gained basics of data modeling and schema design—conceptual/logical modeling, normalization, and structuring datasets for analytics and feature stores.',
                'Performed extensive data cleaning and transformation, including missing-value imputation, outlier detection and handling, normalization/scaling, and automated ETL steps to prepare high-quality datasets for modeling.'
            ]
        }
    ],
    'projects': [
        {
            'name': 'Multi-Agent Reasoning Workflow',
            'period': 'Jan 2025 - Feb 2025',
            'description': 'Chain multiple specialized agents like data extractor, summarizer and decision-engine to solve complex queries.',
            'outcome': 'Chained 4+ agents per request and delivered end-to-end results in under 2 minutes, improving stakeholder satisfaction by 30%.',
            'link':'https://github.com/EonFlash'

        },
        {
            'name': 'Knowledge Base Retrieval Agent',
            'period': 'Feb 2025 - Mar 2025',
            'description': 'Developed an end-to-end RAG agent to ingest and serve insights from mixed document sources via a single API.',
            'outcome': 'Built a FAISS vector database index for 100+ document embeddings, achieving average retrieval times of 650 ms.'
            ,
            'link':'https://github.com/EonFlash'
        },
        {
            'name': 'Alteryx to dbt Migration',
            'period': 'Jul 2024 - Present',
            'description': 'Built an agent-driven pipeline that systematized extraction of Alteryx workflows, converted transformation logic to modular dbt models, and generated dbt tests and documentation.',
            'details': 'Automated 80% of routine transformation translation and test generation; cut initial migration effort by 60% and reduced validation cycles from days to hours.',
            'outcome': 'Demonstrated translation of transformation logic. (POC deployed on client System)'
            ,
            'link':'https://github.com/EonFlash'
        },
        {
            'name': 'Alteryx to KNIME Migration',
            'period': 'Jan 2025 - Present',
            'description': 'Created an agentic migration path to translate Alteryx workflows into KNIME-compatible, Python-based nodes and reusable components without LLM intervention.',
            'details': 'Attained 90% parity for core ETL logic and minimized conversion time by 70% using reusable templates.',
            'outcome': 'Verified parity of core ETL logic and created reusable Python-node templates for KNIME.'
            ,
            'link':'https://github.com/EonFlash'
        },
        {
            'name': 'Data Stage to Big Query Migration',
            'period': 'Jul 2025 - Present',
            'description': 'Applied agents to parse DataStage job metadata, map schemas and transformations to BigQuery SQL, and run validation tests against sample datasets.',
            'outcome': 'Enabled computerized schema mapping and data-quality validation to accelerate migration planning.'
            ,
            'link':'https://github.com/EonFlash'
        }
    ],
    'skills': {
        'technical': 'Python, Flask, SQL, LangChain, Hugging Face, LangGraph, CrewAI, OpenAI APIs, LLMs Transformers, FAISS, Pinecone, ChromaDB, Prompt engineering, Parameter-Efficient FineTuning',
        'soft': 'Strategic problem-solving, Cross-functional collaboration, Technical communication, Critical thinking, Decision-making, Time management',
        'tools': 'AWS S3, Athena, EC2, dbt, Git, Snowflake, KNIME, DataStage, SQL'
    },
    'certifications': [
        {
            'name': 'Oracle - AI Vector Search Professional Certification',
            'date': 'Sep 2025',
            'verification': 'https://catalog-education.oracle.com/ords/certview/sharebadge?id=9318C5DF1E7535A62CF68BD19AB69C0CF51E585A229FE3249A0A95B6614D8424'
            
        },
        {
            'name': 'IGNITE ASP.NET Core & C# Training',
            'issuer': 'LTIMindtree',
            'date': 'Jun 2023'
        }
    ],
    'education': [
        {
            'institution': 'Graphic Era University',
            'location': 'Dehradun, India',
            'degree': 'B.Tech – Computer Science & Engineering',
            'grade': '8.69 CGPA',
            'period': 'Jul 2019 - Jul 2024'
        },
        {
            'institution': 'Scholars Academy',
            'location': 'Roorkee, Uttarakhand, India',
            'degree': 'PCM + CS',
            'details': [
                'CBSE 12th - 70%, Jan 2019',
                'CBSE 10th - 9.4 CGPA, Jan 2017'
            ]
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', data=RESUME_DATA)

@app.route('/download-resume')
def download_resume():
    try:
        resume_path = os.path.join(app.static_folder, 'Chintan_Gaur_Resume.pdf')

        visitor_info = {
            'timestamp': datetime.utcnow().isoformat(),
            'user_agent': request.headers.get('User-Agent'),
            'ip_address': request.headers.get('X-Forwarded-For', request.remote_addr)
        }

        # try:
        #     supabase.table('resume_downloads').insert(visitor_info).execute()
        # except Exception as e:
        #     print(f"Error tracking download: {e}")

        return send_file(
            resume_path,
            as_attachment=True,
            download_name='Chintan_Gaur_Resume.pdf',
            mimetype='application/pdf'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/track-visit', methods=['POST'])
def track_visit():
    # try:
    #     visitor_info = {
    #         'timestamp': datetime.utcnow().isoformat(),
    #         'user_agent': request.headers.get('User-Agent'),
    #         'ip_address': request.headers.get('X-Forwarded-For', request.remote_addr),
    #         'page': request.json.get('page', '/')
    #     }

    #     supabase.table('portfolio_visits').insert(visitor_info).execute()
    #     return jsonify({'success': True}), 200
    # except Exception as e:
    #     print(f"Error tracking visit: {e}")
    #     return jsonify({'error': str(e)}), 500
    pass

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
