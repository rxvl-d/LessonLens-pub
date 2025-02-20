# LessonLens: AI-Enhanced Search Interface for Educational Resources

LessonLens is a browser extension that enhances web search results with educational metadata and contextual information to help teachers find and evaluate educational resources more effectively. The project was developed based on research studying how teachers search for and evaluate online educational resources.

## Key Features

- **SERP Overview**: Provides a visual summary of search results showing educational characteristics like educational level, access type, and source type
- **Metadata Summaries**: Displays structured educational metadata for each search result including teaching objectives, educational level, target audience, and resource type
- **Task-Adaptive Snippets**: Generates enhanced search result descriptions based on the educational context of the search query

## Installation

The extension is available for both Firefox and Chrome browsers. Installation packages can be built from source:

```bash
yarn install
yarn build
```

This will create extension packages in the `build` directory for both browsers.

## Key Implementation Files

Here are the key files and code sections referenced in the research paper:

### Core Extension Components
- [content.tsx](extension/src/content.tsx) - Main content script that injects the extension features into search results
- [SearchResultMetadata/SearchResultMetadata.tsx](extension/src/components/SearchResultMetadata/SearchResultMetadata.tsx) - Component for displaying educational metadata for each result
- [SearchResultsOverlay/StackedSearchResultsOverlay.tsx](extension/src/components/SearchResultsOverlay/StackedSearchResultsOverlay.tsx) - SERP overview visualization component
- [SettingsPopup/SettingsPopup.tsx](extension/src/components/SettingsPopup/SettingsPopup.tsx) - Settings interface for controlling enabled features

### Backend Services
- [api.py](backend/ll/api.py) - Main API endpoints for metadata enrichment and snippet enhancement
- [metadata.py](backend/ll/metadata.py) - Educational metadata extraction service
- [snippets.py](backend/ll/snippets.py) - Task-adaptive snippet generation
- [classifiers.py](backend/ll/classifiers.py) - ML models for classifying educational content

### Key Research Components
- Query term classification model: [models/query_term_classification/](backend/models/query_term_classification/) - Used for understanding educational context from search queries
- Educational metadata fields: `MetadataResult` interface in [types/summary.ts](extension/src/types/summary.ts)
- Confidence visualization: `ConfidenceBar` component in [StackedBarComponents.tsx](extension/src/components/SearchResultsOverlay/StackedBarComponents.tsx)

## Development

To run the extension in development mode:

```bash
# Firefox
yarn load

# Chrome/Edge
yarn load:msedge 

# Watch for changes
yarn watch
```

## License

This project is research code. Please refer to the paper for proper citation if using this work.

## Citation

If you use this code in your research, please cite:

```
@inproceedings{lessonlens2024,
  title={Supporting Teachers through AI-augmented Web Search for Educational Resource Discovery},
  booktitle={awaiting publication},
  year={awaiting publication}
}
```
