import os

# Keep deterministic tests and dependency caches inside the local workspace.
os.environ.setdefault("DSP_CACHEDIR", "/tmp/storm-test-dspy")
os.environ.setdefault("LITELLM_LOCAL_MODEL_COST_MAP", "True")
os.environ.setdefault("HF_HUB_OFFLINE", "1")
