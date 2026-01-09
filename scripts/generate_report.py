#!/usr/bin/env python3
"""
Generate HTML Report for X Trending Topics Analysis
"""

import json
import os
from datetime import datetime
from pathlib import Path

def load_data():
    """Load all analysis data files"""
    base_dir = Path(__file__).parent.parent

    # Load categorized trends
    with open(base_dir / 'data/raw/categorized_trends_20260109_173200.json', 'r', encoding='utf-8') as f:
        categorized = json.load(f)

    # Load sentiment analysis
    with open(base_dir / 'data/processed/sentiment_analysis_20260109_173400.json', 'r', encoding='utf-8') as f:
        sentiment = json.load(f)

    # Load insights
    with open(base_dir / 'data/processed/insights_20260109_173600.json', 'r', encoding='utf-8') as f:
        insights = json.load(f)

    return categorized, sentiment, insights

def generate_html_report(categorized, sentiment, insights):
    """Generate complete HTML report"""

    report_date = "9 Gennaio 2026"

    # Category colors
    category_colors = {
        "Cultura e Spettacolo": "#FF6B6B",
        "Politica Estera": "#4ECDC4",
        "Politica Interna": "#45B7D1",
        "Cronaca Nera": "#96CEB4",
        "Diritti Umani": "#FFEAA7",
        "Economia e Finanza": "#DFE6E9",
        "Geopolitica": "#74B9FF",
        "Cronaca Bianca": "#A29BFE",
        "Società": "#FD79A8",
        "Ambiente": "#55EFC4",
        "Scienza e Tecnologia": "#636E72",
        "Opinioni ed Editoriali": "#E17055",
        "Inchieste e Dossier": "#FDCB6E",
        "Lifestyle e Moda": "#FF7675",
        "Cronaca Giudiziaria": "#B2BEC3",
        "Cronaca Rosa": "#FFA7C4"
    }

    html = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report Trending Topics X Italia - {report_date}</title>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            color: #2d3436;
            background: #f8f9fa;
        }}

        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 3rem 2rem;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        .header h1 {{
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }}

        .header .subtitle {{
            font-size: 1.2rem;
            opacity: 0.9;
            font-weight: 300;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }}

        .nav {{
            background: white;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            padding: 1rem 2rem;
            margin-bottom: 2rem;
        }}

        .nav ul {{
            list-style: none;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 2rem;
        }}

        .nav a {{
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }}

        .nav a:hover {{
            color: #764ba2;
        }}

        .section {{
            background: white;
            border-radius: 12px;
            padding: 2.5rem;
            margin-bottom: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}

        .section h2 {{
            color: #667eea;
            font-size: 2rem;
            margin-bottom: 1.5rem;
            padding-bottom: 0.8rem;
            border-bottom: 3px solid #667eea;
        }}

        .section h3 {{
            color: #2d3436;
            font-size: 1.5rem;
            margin: 2rem 0 1rem 0;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }}

        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 2rem;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
        }}

        .stat-card .number {{
            font-size: 3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }}

        .stat-card .label {{
            font-size: 1rem;
            opacity: 0.9;
        }}

        .trend-item {{
            border-left: 4px solid #667eea;
            padding: 1.5rem;
            margin: 1rem 0;
            background: #f8f9fa;
            border-radius: 8px;
            transition: transform 0.2s, box-shadow 0.2s;
        }}

        .trend-item:hover {{
            transform: translateX(4px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}

        .trend-item h4 {{
            color: #667eea;
            font-size: 1.3rem;
            margin-bottom: 0.5rem;
        }}

        .trend-meta {{
            display: flex;
            gap: 1.5rem;
            margin: 0.8rem 0;
            flex-wrap: wrap;
        }}

        .trend-meta span {{
            color: #636e72;
            font-size: 0.9rem;
        }}

        .sentiment-badge {{
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
        }}

        .sentiment-positive {{
            background: #00b894;
            color: white;
        }}

        .sentiment-negative {{
            background: #d63031;
            color: white;
        }}

        .sentiment-neutral {{
            background: #636e72;
            color: white;
        }}

        .sentiment-mixed {{
            background: #fdcb6e;
            color: #2d3436;
        }}

        .category-section {{
            margin: 2rem 0;
            padding: 2rem;
            background: #f8f9fa;
            border-radius: 12px;
            border-left: 6px solid #667eea;
        }}

        .category-header {{
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
        }}

        .category-icon {{
            font-size: 2rem;
        }}

        .insight-card {{
            background: white;
            border-radius: 12px;
            padding: 2rem;
            margin: 1.5rem 0;
            border-left: 6px solid #00b894;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}

        .insight-card h4 {{
            color: #00b894;
            font-size: 1.3rem;
            margin-bottom: 1rem;
        }}

        .insight-importance {{
            display: inline-block;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-left: 0.5rem;
        }}

        .importance-high {{
            background: #d63031;
            color: white;
        }}

        .importance-critical {{
            background: #e17055;
            color: white;
        }}

        .importance-medium {{
            background: #fdcb6e;
            color: #2d3436;
        }}

        .keywords {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }}

        .keyword {{
            background: #e0e7ff;
            color: #667eea;
            padding: 0.4rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
        }}

        .chart-container {{
            margin: 2rem 0;
            background: white;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
        }}

        th {{
            background: #667eea;
            color: white;
            padding: 1rem;
            text-align: left;
            font-weight: 600;
        }}

        td {{
            padding: 1rem;
            border-bottom: 1px solid #dfe6e9;
        }}

        tr:hover {{
            background: #f8f9fa;
        }}

        .footer {{
            background: #2d3436;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
            margin-top: 4rem;
        }}

        .footer a {{
            color: #667eea;
            text-decoration: none;
        }}

        .back-to-top {{
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: #667eea;
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            transition: transform 0.3s;
        }}

        .back-to-top:hover {{
            transform: translateY(-4px);
        }}

        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 1.8rem;
            }}

            .stats-grid {{
                grid-template-columns: 1fr;
            }}

            .nav ul {{
                flex-direction: column;
                gap: 1rem;
            }}

            .section {{
                padding: 1.5rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 Report Trending Topics X Italia</h1>
        <div class="subtitle">{report_date} - Analisi Completa</div>
    </div>

    <nav class="nav">
        <ul>
            <li><a href="#executive-summary">Executive Summary</a></li>
            <li><a href="#dashboard">Dashboard</a></li>
            <li><a href="#by-category">Per Categoria</a></li>
            <li><a href="#sentiment">Sentiment</a></li>
            <li><a href="#insights">Insights</a></li>
            <li><a href="#methodology">Metodologia</a></li>
        </ul>
    </nav>

    <div class="container">
        <!-- EXECUTIVE SUMMARY -->
        <section id="executive-summary" class="section">
            <h2>Executive Summary</h2>

            <div class="stats-grid">
                <div class="stat-card">
                    <div class="number">{len(categorized['categorized_trends'])}</div>
                    <div class="label">Trending Topics Analizzati</div>
                </div>
                <div class="stat-card">
                    <div class="number">{int(sentiment['overall_statistics']['total_tweet_volume']/1000)}K</div>
                    <div class="label">Tweet Totali</div>
                </div>
                <div class="stat-card">
                    <div class="number">7</div>
                    <div class="label">Categorie Attive</div>
                </div>
                <div class="stat-card">
                    <div class="number">{sentiment['overall_statistics']['overall_avg_sentiment']:.2f}</div>
                    <div class="label">Sentiment Medio</div>
                </div>
            </div>

            <h3>Highlights Principali</h3>
            <ul style="line-height: 2; font-size: 1.1rem;">
                <li><strong>Categoria Dominante:</strong> Cultura e Spettacolo (60% dei trend)</li>
                <li><strong>Tema più virale:</strong> Iran con 400K+ tweet aggregati (Pahlavi + #Iran)</li>
                <li><strong>Sentiment generale:</strong> Negativo (-0.23), trainato da temi politici e cronaca</li>
                <li><strong>Massima polarizzazione:</strong> Acca Larentia (0.95) - memoria storica italiana</li>
                <li><strong>Trend emergente:</strong> Importazione "culture wars" USA (Charlie Kirk 237K tweet)</li>
            </ul>
        </section>
"""

    # Add Category Distribution Chart
    html += """
        <!-- DASHBOARD CATEGORIE -->
        <section id="dashboard" class="section">
            <h2>Dashboard Categorie</h2>
            <div class="chart-container" id="category-pie"></div>
            <div class="chart-container" id="category-bars"></div>
        </section>
"""

    # Add Trends by Category
    html += """
        <!-- TOP TRENDING PER CATEGORIA -->
        <section id="by-category" class="section">
            <h2>Top Trending Topics per Categoria</h2>
"""

    # Group trends by category
    trends_by_cat = {}
    for trend in categorized['categorized_trends']:
        cat = trend['primary_category']
        if cat not in trends_by_cat:
            trends_by_cat[cat] = []
        trends_by_cat[cat].append(trend)

    # Sort categories by number of trends
    sorted_cats = sorted(trends_by_cat.items(), key=lambda x: len(x[1]), reverse=True)

    category_icons = {
        "Cultura e Spettacolo": "🎭",
        "Politica Estera": "🌍",
        "Politica Interna": "🏛️",
        "Cronaca Nera": "🚨",
        "Diritti Umani": "✊",
        "Economia e Finanza": "💰",
        "Cronaca Bianca": "📰"
    }

    for cat_name, trends in sorted_cats:
        icon = category_icons.get(cat_name, "📌")
        html += f"""
            <div class="category-section">
                <div class="category-header">
                    <span class="category-icon">{icon}</span>
                    <h3>{cat_name} ({len(trends)} trend)</h3>
                </div>
"""

        # Get sentiment data for this category
        cat_sentiment = sentiment['sentiment_by_category'].get(cat_name, {})

        if cat_sentiment:
            html += f"""
                <p><strong>Sentiment medio categoria:</strong> <span class="sentiment-badge sentiment-{'positive' if cat_sentiment['avg_sentiment_score'] > 0 else 'negative' if cat_sentiment['avg_sentiment_score'] < 0 else 'neutral'}">{cat_sentiment['avg_sentiment_score']:.2f}</span></p>
                <p><strong>Polarizzazione:</strong> {cat_sentiment['polarization_index']:.2f}</p>
"""

        for trend in sorted(trends, key=lambda x: x['tweet_volume'], reverse=True):
            # Get sentiment for this specific topic
            topic_sentiment = next((t for t in sentiment['sentiment_by_topic'] if t['topic_name'] == trend['name']), None)

            sentiment_class = "sentiment-neutral"
            if topic_sentiment:
                score = topic_sentiment['sentiment_score']
                if score > 0.3:
                    sentiment_class = "sentiment-positive"
                elif score < -0.3:
                    sentiment_class = "sentiment-negative"
                elif abs(score) <= 0.3:
                    sentiment_class = "sentiment-mixed"

            sentiment_value = f"{topic_sentiment['sentiment_score']:.2f}" if topic_sentiment else "N/A"
            html += f"""
                <div class="trend-item">
                    <h4>{trend['name']}</h4>
                    <div class="trend-meta">
                        <span><strong>Volume:</strong> {trend['tweet_volume']:,} tweet</span>
                        <span class="sentiment-badge {sentiment_class}"><strong>Sentiment:</strong> {sentiment_value}</span>
                        <span><strong>Confidence:</strong> {trend['confidence_score']:.0%}</span>
                    </div>
                    <p>{trend['description']}</p>
                    <div class="keywords">
"""
            for keyword in trend['relevant_keywords'][:5]:
                html += f'<span class="keyword">{keyword}</span>'

            html += """
                    </div>
                </div>
"""

        html += """
            </div>
"""

    html += """
        </section>
"""

    # Add Sentiment Analysis Section
    html += """
        <!-- ANALISI SENTIMENT -->
        <section id="sentiment" class="section">
            <h2>Analisi del Sentiment per Categoria</h2>

            <h3>Confronto Sentiment tra Categorie</h3>
            <div class="chart-container" id="sentiment-comparison"></div>

            <h3>Distribuzione Sentiment Generale</h3>
            <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                Il sentiment complessivo della giornata è <strong>negativo (-0.23)</strong>,
                con il <strong>{:.1f}%</strong> dei contenuti classificati come negativi.
            </p>

            <table>
                <thead>
                    <tr>
                        <th>Categoria</th>
                        <th>Sentiment Medio</th>
                        <th>Polarizzazione</th>
                        <th>Mood</th>
                    </tr>
                </thead>
                <tbody>
""".format(sentiment['overall_statistics']['overall_distribution']['negative'])

    for item in sentiment['category_comparison']['sentiment_spectrum']:
        mood_emoji = "😊" if item['score'] > 0.3 else "😟" if item['score'] < -0.3 else "😐"
        html += f"""
                    <tr>
                        <td><strong>{item['category']}</strong></td>
                        <td>{item['score']:.2f}</td>
                        <td>{sentiment['sentiment_by_category'][item['category']]['polarization_index']:.2f}</td>
                        <td>{mood_emoji} {item['mood']}</td>
                    </tr>
"""

    html += """
                </tbody>
            </table>

            <h3>Topic più Polarizzati</h3>
            <ul style="line-height: 2; font-size: 1.1rem;">
"""

    for topic in sentiment['sentiment_trends']['most_polarized_topics'][:5]:
        html += f"                <li>{topic}</li>\n"

    html += """
            </ul>
        </section>
"""

    # Add Insights Section
    html += """
        <!-- INSIGHT SOCIOLOGICI -->
        <section id="insights" class="section">
            <h2>Insight Sociologici</h2>

            <h3>Key Insights</h3>
"""

    for insight in insights['key_insights']:
        importance_class = f"importance-{insight['importance']}"
        html += f"""
            <div class="insight-card">
                <h4>
                    {insight['insight']}
                    <span class="insight-importance {importance_class}">{insight['importance'].upper()}</span>
                </h4>
                <p><strong>Categoria:</strong> {insight['category']}</p>
                <p>{insight['explanation']}</p>
            </div>
"""

    html += """
            <h3>Analisi di Polarizzazione</h3>
            <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                Le categorie più polarizzate mostrano echo chambers fortemente separate e poco dialogo costruttivo.
            </p>

            <div class="chart-container" id="polarization-chart"></div>

            <h3>Trend Emergenti</h3>
"""

    for trend in insights['emerging_trends']:
        html += f"""
            <div class="insight-card" style="border-left-color: #fdcb6e;">
                <h4 style="color: #fdcb6e;">{trend['topic']}</h4>
                <p><strong>Categoria:</strong> {trend['category']}</p>
                <p><strong>Segnale:</strong> {trend['signal_strength']}</p>
                <p>{trend['description']}</p>
                <p><em>Implicazione: {trend['implication']}</em></p>
            </div>
"""

    html += """
            <h3>Cross-Category Analysis</h3>
            <p style="font-size: 1.1rem; margin: 1.5rem 0;">
                Alcuni topic attraversano multiple categorie, creando connessioni tra ambiti diversi del dibattito pubblico.
            </p>
"""

    for cross in insights['cross_category_trends']:
        cats = ", ".join(cross['categories'])
        html += f"""
            <div class="trend-item">
                <h4>{cross['topic']}</h4>
                <p><strong>Categorie coinvolte:</strong> {cats}</p>
                <p><strong>Volume totale:</strong> {cross['total_volume']:,} tweet</p>
                <p>{cross['analysis']}</p>
            </div>
"""

    html += """
        </section>
"""

    # Add Methodology
    html += """
        <!-- METODOLOGIA -->
        <section id="methodology" class="section">
            <h2>Metodologia e Note Tecniche</h2>

            <h3>Raccolta Dati</h3>
            <p>I dati sono stati raccolti manualmente dalle principali fonti di trending topics di X (Twitter) Italia
            in data 9 gennaio 2026. Il dataset include 20 trending topics con volumi stimati.</p>

            <h3>Categorizzazione</h3>
            <p>Ogni trending topic è stato categorizzato in una delle 16 categorie del blog tramite analisi semantica
            del contenuto e delle keyword associate. La categorizzazione ha raggiunto un confidence score medio di 0.93.</p>

            <h3>Sentiment Analysis</h3>
            <p>Il sentiment è stato analizzato su scala da -1 (molto negativo) a +1 (molto positivo),
            con classificazione in positivo, negativo, neutro. L'indice di polarizzazione (0-1) misura
            il livello di divisione dell'opinione pubblica sul topic.</p>

            <h3>Limitazioni</h3>
            <ul style="line-height: 2;">
                <li>Dati raccolti manualmente, non tramite API diretta</li>
                <li>Volumi tweet stimati/arrotondati per alcuni trend</li>
                <li>Network analysis e dati influencer simulati</li>
                <li>Dati geografici e temporali stimati</li>
                <li>Nessun dato storico per confronti temporali</li>
            </ul>

            <h3>Privacy e Etica</h3>
            <p>Tutti i dati presentati sono pubblici e aggregati. Nessun dato personale identificabile è stato raccolto o pubblicato.
            L'analisi rispetta i termini di servizio di X e le normative sulla privacy.</p>

            <h3>Codice e Documentazione</h3>
            <p>Questo progetto è open source. Per maggiori informazioni, consulta il repository GitHub.</p>
        </section>
    </div>

    <div class="footer">
        <p>Report generato automaticamente il {datetime.now().strftime('%d/%m/%Y alle %H:%M')}</p>
        <p style="margin-top: 1rem;">Progetto Analisi_social | Powered by Python + Plotly</p>
        <p style="margin-top: 1rem; font-size: 0.9rem;">
            <a href="https://github.com">GitHub</a> |
            <a href="#executive-summary">Torna su</a>
        </p>
    </div>

    <div class="back-to-top" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">
        ↑
    </div>

    <script>
        // Category Distribution Pie Chart
        const categoryData = {json.dumps(list(insights['category_distribution'].values()))};
        const categoryLabels = {json.dumps(list(insights['category_distribution'].keys()))};
        const categoryValues = categoryData.map(c => c.count);

        const pieData = [{{
            values: categoryValues,
            labels: categoryLabels,
            type: 'pie',
            hole: 0.4,
            marker: {{
                colors: ['#FF6B6B', '#4ECDC4', '#96CEB4', '#FFEAA7', '#DFE6E9', '#45B7D1', '#A29BFE']
            }},
            textinfo: 'label+percent',
            textposition: 'outside',
            automargin: true
        }}];

        const pieLayout = {{
            title: 'Distribuzione Trend per Categoria',
            height: 500,
            showlegend: true,
            font: {{
                family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto',
                size: 14
            }}
        }};

        Plotly.newPlot('category-pie', pieData, pieLayout, {{responsive: true}});

        // Category Bars
        const barData = [{{
            x: categoryLabels,
            y: categoryValues,
            type: 'bar',
            marker: {{
                color: ['#FF6B6B', '#4ECDC4', '#96CEB4', '#FFEAA7', '#DFE6E9', '#45B7D1', '#A29BFE'],
                line: {{
                    width: 1,
                    color: '#2d3436'
                }}
            }}
        }}];

        const barLayout = {{
            title: 'Numero di Trend per Categoria',
            xaxis: {{
                title: 'Categoria',
                tickangle: -45
            }},
            yaxis: {{
                title: 'Numero di Trend'
            }},
            height: 500,
            font: {{
                family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto',
                size: 12
            }}
        }};

        Plotly.newPlot('category-bars', barData, barLayout, {{responsive: true}});

        // Sentiment Comparison
        const sentimentCategories = {json.dumps([item['category'] for item in sentiment['category_comparison']['sentiment_spectrum']])};
        const sentimentScores = {json.dumps([item['score'] for item in sentiment['category_comparison']['sentiment_spectrum']])};

        const sentimentData = [{{
            x: sentimentCategories,
            y: sentimentScores,
            type: 'bar',
            marker: {{
                color: sentimentScores.map(score =>
                    score > 0.3 ? '#00b894' :
                    score < -0.3 ? '#d63031' :
                    '#636e72'
                )
            }}
        }}];

        const sentimentLayout = {{
            title: 'Sentiment Medio per Categoria',
            xaxis: {{
                title: 'Categoria',
                tickangle: -45
            }},
            yaxis: {{
                title: 'Sentiment Score (-1 a +1)',
                zeroline: true,
                zerolinewidth: 2,
                zerolinecolor: '#636e72'
            }},
            height: 500,
            font: {{
                family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto',
                size: 12
            }},
            shapes: [{{
                type: 'line',
                x0: -0.5,
                x1: sentimentCategories.length - 0.5,
                y0: 0,
                y1: 0,
                line: {{
                    color: '#636e72',
                    width: 2,
                    dash: 'dash'
                }}
            }}]
        }};

        Plotly.newPlot('sentiment-comparison', sentimentData, sentimentLayout, {{responsive: true}});

        // Polarization Chart
        const polarizationCategories = {json.dumps([item['category'] for item in sentiment['category_comparison']['polarization_ranking']])};
        const polarizationScores = {json.dumps([item['index'] for item in sentiment['category_comparison']['polarization_ranking']])};

        const polarizationData = [{{
            x: polarizationScores,
            y: polarizationCategories,
            type: 'bar',
            orientation: 'h',
            marker: {{
                color: polarizationScores.map(score =>
                    score > 0.8 ? '#d63031' :
                    score > 0.6 ? '#e17055' :
                    score > 0.4 ? '#fdcb6e' :
                    '#00b894'
                )
            }}
        }}];

        const polarizationLayout = {{
            title: 'Indice di Polarizzazione per Categoria (0 = consenso, 1 = massima divisione)',
            xaxis: {{
                title: 'Indice di Polarizzazione',
                range: [0, 1]
            }},
            yaxis: {{
                title: ''
            }},
            height: 500,
            font: {{
                family: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto',
                size: 12
            }}
        }};

        Plotly.newPlot('polarization-chart', polarizationData, polarizationLayout, {{responsive: true}});
    </script>
</body>
</html>
"""

    return html

def main():
    """Main function to generate report"""
    print("Loading data...")
    categorized, sentiment, insights = load_data()

    print("Generating HTML report...")
    html_content = generate_html_report(categorized, sentiment, insights)

    # Save report
    output_dir = Path(__file__).parent.parent / 'reports' / 'archive'
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / 'report_20260109.html'

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✓ Report generated successfully!")
    print(f"✓ Saved to: {output_file}")
    print(f"✓ File size: {output_file.stat().st_size / 1024:.1f} KB")
    print(f"\nOpen the report in your browser:")
    print(f"file://{output_file.absolute()}")

    return str(output_file)

if __name__ == "__main__":
    main()
