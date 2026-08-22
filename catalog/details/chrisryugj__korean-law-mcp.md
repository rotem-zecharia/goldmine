# chrisryugj/korean-law-mcp

법제처 국가법령정보를 LLM에서 바로 조회하는 MCP 서버. 법령·판례·조례 검색과 인용 검증 / MCP server for Korean law — search statutes, precedents, and ordinances, and verify citations

## tools

법제처 OPEN API가 **`Referer` 헤더 없는 요청을 OC 키 유효 여부와 무관하게 거부**("사용자 정보 검증 실패")하는 문제 대응. `law.go.kr` 계열 호스트 호출 시 기본 `Referer`를 자동 주입한다(`LAW_REFERER`로 override). IP/도메인 등록 문제로 오인되기 쉬운 증상의 실제 근본 원인이었음 — IP 등록을 했는데도 모든 검색이 실패하던 케이스를 해결. (외부 PR #45)
