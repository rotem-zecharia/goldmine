# chrisryugj/kordoc

모두 파싱해버리겠다 — HWP·HWPX·PDF·Office 문서를 Markdown으로. 양식 자동 채우기와 신구대조를 갖춘 CLI·MCP 서버 / Convert Korean documents (HWP, HWPX, PDF, Office) to Markdown — CLI and MCP server with form filling and diff

## tools

### 핵심 함수

| 함수 | 설명 |
|------|------|
| `parse(buffer, options?)` | 포맷 자동 감지 → Markdown + IRBlock[] |
| `parseHwpx(buffer, options?)` | HWPX 전용 |
| `parseHwp(buffer, options?)` | HWP 5.x 전용 |
| `parseHwp3(buffer, options?)` | HWP 3.x (1996~2002 구버전) 전용 |
| `parsePdf(buffer, options?)` | PDF 전용 |
| `parseXlsx(buffer, options?)` | XLSX 전용 |
| `parseXls(buffer, options?)` | XLS (Excel 97~2003, BIFF8) 전용 |
| `parseDocx(buffer, options?)` | DOCX 전용 |
| `parseHwpml(buffer, options?)` | HWPML (XML 기반 HWP) 전용 |
| `parseImage(buffer, options?)` | 이미지(PNG/JPG/WebP) 전용 — 내장 OCR 상시 적용 (v4.2.1) |
| `detectFormat(buffer)` | `"hwpx" \| "hwp" \| "hwp3" \| "hwpml" \| "pdf" \| "xlsx" \| "xls" \| "docx" \| "image" \| "unknown"` |

### 고급 함수

| 함수 | 설명 |
|------|------|
| `compare(bufferA, bufferB, options?)` | IR 레벨 문서 비교 |
| `extractFormFields(blocks)` | IRBlock[]에서 양식 필드 인식 |
| `extractFormSchema(blocks)` | 양식 필드 인식 + 타입/필수/빈값 추론 (v3.1) |
| `fillForm(input, values, outputFormat?)` | 양식 템플릿에 값 채우기 — outputFormat: `"markdown"`(기본)/`"hwpx"`/`"hwpx-preserve"`, 반환 `{ output, format, fill }` |
| `fillFormFields(blocks, values)` | IRBlock[] 기반 필드 값 교체 |
| `fillHwpx(buffer, values)` | HWPX XML 직접 조작 (원본 서식 보존) |
| `extractClickHereFields(buffer)` | HWPX 누름틀(CLICK_HERE) 필드 조사 — 이름·안내문 목록 (v4.3) |
| `resolveBuiltinTemplate(name)` / `readBuiltinTemplate(t)` | 내장 표준 기안문 서식 조회·로드 (`gian`/`gian-simple`, v4.3) |
| `patchHwpx(original, editedMarkdown, options?)` | 편집 마크다운 → 원본 HWPX 서식 보존 in-place 패치 (v3.0) |
| `patchHwp(original, editedMarkdown, options?)` | 편집 마크다운 → 원본 HWP 5.x 바이너리 서식 보존 패치 (v3.0.1) |
| `openHwpxDocument(bytes, options?)` | 에디터용 블록 단위 증분 패치 세션 `HwpxSession` (v3.1) |
| `patchHwpxBlocks(bytes, edits, options?)` | 세션 없이 블록 편집 1회 패치 (v3.1) |
| `markdownToHwpx(markdown, options?)` | Markdown → HWPX 역변환 (테마·서식 프로필·페이지 옵션 지원) |
| `hwpxToProfile(buffer)` | 참조 HWPX → 표 서식 프로필 JSON — `markdownToHwpx(md, { profile })` 로 재현 (v3.18) |
| `markdownToPdf(markdown, options?)` | Markdown → PDF 생성 (Print Renderer — `puppeteer-core` 별도 설치 필요) |
| `blocksToPdf(blocks, options?)` | IRBlock[] → PDF 생성 (동일하게 `puppeteer-core` 필요) |
| `renderHtml(blocks, options?)` | IRBlock[] → 인쇄용 HTML (puppeteer 불필요) |
| `renderHwpxToSvg(buffer, options?)` | HWPX → 레이아웃 보존 SVG — 다페이지·형광펜·도형, 캐시 없으면 `reflow` (v3.10~15) |
| `placeSealHwpx(buffer, seals)` | 도장/서명 이미지를 앵커 문구 위에 부유 배치 (v3.16) |
| `validateHwpx(buffer)` | HWPX 구조 검증 — ZIP·mimetype·필수 파트·XML 웰폼드 (v3.16) |
| `lintGongmunText(text)` | 공문서 표기법 검수 13룰 — 텍스트/마크다운 입력 (v4.0.1) |
| `redactMarkdown(text, options?)` / `redactText(...)` | 개인정보 탐지 + 마스킹 (기본 룰: 주민번호·전화·이메일·카드·계좌, v4.1) |
| `blocksToChunks(blocks, options?)` | RAG용 구조 청크 — 헤딩·개조식 위계 breadcrumb + 표 독립 청크 (v4.1) |
| `blocksToMarkdown(blocks)` | IRBlock[] → Markdown 문자열 |
| `blocksToPages(blocks)` | IRBlock[] → `[{ pageNumber, markdown }]` 페이지별 마크다운 (v4.8) |

### 타입

```typescript
import type {
  ParseResult, ParseSuccess, ParseFailure, FileType,
  IRBlock, IRBlockType, IRTable, IRCell, CellContext,
  DocumentMetadata, ParseOptions, ErrorCode, OutlineItem,
  DiffResult, BlockDiff, CellDiff, DiffChangeType,
  FormField, FormResult, FormFieldType, FormFieldSchema, FormSchemaResult,
  FillResult, HwpxFillResult, FillOutputFormat, FillFormOutput,
  ClickHereField, BuiltinTemplate,
  PatchOptions, PatchResult, PatchSkip,
  HwpxTheme, MarkdownToHwpxOptions, PageOptions,
  PrintPreset, PrintOptions, PageMargin,
  RenderSvgOptions, RenderSvgResult,
  SealOp, SealPlacement, PlaceSealResult,
  ValidateResult, ValidateIssue,
  RedactRule, RedactOptions, RedactHit, RedactTextResult,
  DocChunk, ChunkOptions, GongmunLintFinding,
  OcrProvider, WatchOptions,
} from "kordoc"
```

## 지원 포맷

| 포맷 | 엔진 | 특징 |
|------|------|------|
| **HWPX** (한컴 2020+) | ZIP + XML DOM | 매니페스트, 중첩 테이블, 병합 셀, 손상 ZIP 복구, 조판 캐시 기반 실제 페이지 경계, 열기 암호 |
| **HWP 5.x** (한컴 레거시) | OLE2 + CFB | 배포용 복호화, 열기 암호, 손상 CFB 복구, 각주/하이퍼링크, 21종 제어문자, 이미지 추출, 실제 페이지 경계 |
| **HWP 3.x** (1996~2002) | 단일 binary | 상용조합형→유니코드, 5,
