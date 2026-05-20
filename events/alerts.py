from ui.incident_art import PROD_DOWN_SUCCESS, PROD_DOWN_FAIL, CPU_SPIKE_SUCCESS, CPU_SPIKE_FAIL, LATENCY_SUCCESS, LATENCY_FAIL
incidents = [{"alert": "🚨 PROD DOWN", "response": "You saved PROD in {time:.4f}s!", "success_art": PROD_DOWN_SUCCESS, "fail_art": PROD_DOWN_FAIL},
             {"alert": "🔥 CPU SPIKE", "response": "You fixed the CPU spike in {time:.4f}s!", "success_art": CPU_SPIKE_SUCCESS, "fail_art": CPU_SPIKE_FAIL},
             {"alert": "⏱️ LATENCY", "response": "You fixed the Latency issue in {time:.4f}s!", "success_art": LATENCY_SUCCESS, "fail_art": LATENCY_FAIL}
]
