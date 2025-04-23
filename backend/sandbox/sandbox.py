import os
from typing import Optional

from dotenv import load_dotenv

from agentpress.tool import Tool
from utils.logger import logger
from utils.files_utils import clean_path
from utils.thread_manager import ThreadManager

load_dotenv()

logger.warning("Daytona sandbox integration is disabled for this deployment.")

# Stubbed out to prevent backend crashes
async def get_or_start_sandbox(sandbox_id: str):
    logger.warning("get_or_start_sandbox() called, but Daytona is disabled.")
    return None

def start_supervisord_session(sandbox):
    logger.warning("start_supervisord_session() called, but Daytona is disabled.")

def create_sandbox(password: str, sandbox_id: str = None):
    logger.warning("create_sandbox() called, but Daytona is disabled.")
    return None

class SandboxToolsBase(Tool):
    """Stub for sandbox tools when Daytona is disabled."""

    def __init__(self, project_id: str, thread_manager: Optional[ThreadManager] = None):
        super().__init__()
        self.project_id = project_id
        self.thread_manager = thread_manager
        self.workspace_path = "/workspace"
        self._sandbox = None
        self._sandbox_id = None
        self._sandbox_pass = None

    async def _ensure_sandbox(self):
        logger.warning(f"_ensure_sandbox() called for project {self.project_id}, but Daytona is disabled.")
        return None

    @property
    def sandbox(self):
        raise RuntimeError("Sandbox access is disabled. Daytona integration is not available.")

    @property
    def sandbox_id(self):
        raise RuntimeError("Sandbox ID is unavailable. Daytona integration is not enabled.")

    def clean_path(self, path: str) -> str:
        cleaned_path = clean_path(path, self.workspace_path)
        logger.debug(f"Cleaned path: {path} -> {cleaned_path}")
        return cleaned_path
