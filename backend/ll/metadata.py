from ll.classifiers import *
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict
import logging
from threading import Lock

log = logging.getLogger("metadata")

class MetadataEnricher:
    def __init__(self, web_page_cache):
        self.web_page_cache = web_page_cache

    def enrich(self, serp_data: List[Dict]) -> List[Dict]:
        # Thread-safe counters using Lock
        
        def process_single_result(result: Dict) -> Dict:
            """Process a single search result and generate metadata."""
            metadata_part = {
                'url': (url := result['url'])
            }
            title = result['title']
            description = result['description']
            
            try:
                content = self.web_page_cache.fetch_text(url)
                
                if content:
                    content = content[:5000]
                else:
                    content = f"Title: {title}\nDescription: {description}"
                
                response = content_based_gpt_metadata_inference(url, content)
                if response:
                    metadata_fields = [
                        'assesses', 'teaches', 'educational_level', 
                        'educational_role', 'educational_use', 
                        'learning_resource_type'
                    ]
                    for field in metadata_fields:
                        metadata_part[field] = response[field]
                    return metadata_part
                    
            except Exception as e:
                logging.error(f"Error processing {url}: {str(e)}")
                return None
                
            return None

        metadatas = []
        # Use ThreadPoolExecutor since this is I/O bound
        with ThreadPoolExecutor(max_workers=10) as executor:
            # Submit all tasks
            future_to_url = {
                executor.submit(process_single_result, result): result['url']
                for result in serp_data[:2]
            }
            
            # Collect results as they complete
            for future in as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    metadata = future.result()
                    if metadata:
                        metadatas.append(metadata)
                except Exception as e:
                    logging.error(f"Error processing future for {url}: {str(e)}")
                    continue

        # Calculate and print hit ratio
        return metadatas