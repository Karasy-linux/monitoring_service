import pandas as pd
import json
def analyze_data():
    data = pd.read_json('system_history.jsonl', lines=True)
    # Example analysis: Calculate average CPU and RAM usage
    avg_cpu = data['cpu_total'].mean()
    avg_ram = data['ram_percent'].mean()

    peak_cpu = data['cpu_total'].max()
    peak_ram = data['ram_percent'].max()

    data['large_processes'] = data['top_processes'].apply(lambda x: [proc['name'] 
            for proc in x if proc.get('cpu_percent', 0) > 20.0]
                if isinstance(x, list) else [])
    
    report = {
        'average_cpu': avg_cpu,
        'average_ram': avg_ram,
        'peak_cpu': peak_cpu,
        'peak_ram': peak_ram,
        'large_processes': data['large_processes'].tolist()
    }
    with open('analysis_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=4)
    return data, avg_cpu, avg_ram, peak_cpu, peak_ram, 

print("Analyzing system history data...")
data, avg_cpu, avg_ram, peak_cpu, peak_ram,  = analyze_data()
                                                      
print("\n\nAnalysis complete.")

print("\n\nDetailed Data:")
print(data)
print(f'\nAverage CPU Usage: {avg_cpu:.2f}%')
print(f'\nAverage RAM Usage: {avg_ram:.2f}%')
print(f'\nPeak CPU Usage: {peak_cpu:.2f}%')
print(f'\nPeak RAM Usage: {peak_ram:.2f}%')



