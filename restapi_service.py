import uvicorn
import sys

import restapi.main

def main():
    uvicorn.run(
            "restapi.main:app",
            host="localhost",
            port=8000,
            reload=True
    )

if __name__ == "__main__":
    main()
